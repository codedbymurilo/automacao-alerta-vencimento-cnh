"""
Automação de Verificação de CNH - Sistema de Alerta de Vencimento

Lê um arquivo Excel com dados de CNH, verifica quais estão próximas de vencer
e envia alertas por email para o setor de frotas.
"""

import pandas as pd
import smtplib
import os
import schedule
import time
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from pathlib import Path

from config import Config
from utils import (
    criar_pasta_se_nao_existir,
    obter_caminho_relatorio,
    gerar_nome_relatorio,
    validar_arquivo_existe,
    obter_timestamp_legivel,
    limpar_relatorios_antigos,
)


class AutomacaoCNH:
    """Classe responsável pela automação de verificação de CNH."""

    def __init__(self):
        """Inicializa a automação com as configurações."""
        self.config = Config()
        self._preparar_ambiente()

    def _preparar_ambiente(self):
        """Prepara o ambiente (cria pastas necessárias, valida config)."""
        erros = Config.validar()
        if erros:
            print("\n⚠️  Erros de Configuração:")
            for erro in erros:
                print(f"   {erro}")
            print("\n📝 Edite o arquivo .env com as configurações necessárias!")
            raise ValueError("Configurações incompletas")

        criar_pasta_se_nao_existir(self.config.PASTA_RELATORIOS)

    def ler_arquivo_cnh(self):
        """
        Lê o arquivo Excel com dados de CNH.

        Returns:
            pd.DataFrame: DataFrame com colunas [Nome, CNH, Validade] ou None se erro
        """
        if not validar_arquivo_existe(self.config.ARQUIVO_CNH):
            return None

        try:
            df = pd.read_excel(self.config.ARQUIVO_CNH)
            df.columns = ['Nome', 'CNH', 'Validade']
            return df
        except Exception as e:
            print(f"❌ Erro ao ler arquivo: {e}")
            return None

    def verificar_cnhs_vencendo(self, df):
        """
        Verifica quais CNHs vencem em breve.

        Args:
            df (pd.DataFrame): DataFrame com dados de CNH

        Returns:
            pd.DataFrame: DataFrame filtrado com CNHs próximas de vencer
        """
        df['Validade'] = pd.to_datetime(
            df['Validade'], format='%d/%m/%Y', errors='coerce'
        )

        hoje = datetime.now().date()
        data_limite = hoje + timedelta(days=self.config.DIAS_ALERTA)

        cnhs_vencendo = df[
            (df['Validade'].dt.date >= hoje) &
            (df['Validade'].dt.date <= data_limite)
        ].copy()

        if len(cnhs_vencendo) > 0:
            cnhs_vencendo['Dias_para_vencer'] = (
                cnhs_vencendo['Validade'].dt.date - hoje
            ).apply(lambda x: x.days)
            cnhs_vencendo = cnhs_vencendo.sort_values('Dias_para_vencer')

        return cnhs_vencendo

    def criar_planilha_relatorio(self, cnhs_vencendo):
        """
        Cria um arquivo Excel com as CNHs próximas de vencer.

        Args:
            cnhs_vencendo (pd.DataFrame): DataFrame com CNHs a alertar

        Returns:
            str: Caminho completo do arquivo criado ou None
        """
        if len(cnhs_vencendo) == 0:
            return None

        nome_arquivo = gerar_nome_relatorio()
        caminho_completo = obter_caminho_relatorio(
            self.config.PASTA_RELATORIOS, nome_arquivo
        )

        try:
            cnhs_vencendo_copia = cnhs_vencendo.copy()
            cnhs_vencendo_copia['Validade'] = cnhs_vencendo_copia['Validade'].dt.strftime(
                '%d/%m/%Y'
            )

            with pd.ExcelWriter(caminho_completo, engine='openpyxl') as writer:
                cnhs_vencendo_copia.to_excel(
                    writer, index=False, sheet_name='CNHs Vencendo'
                )

                worksheet = writer.sheets['CNHs Vencendo']
                for idx, col in enumerate(cnhs_vencendo_copia.columns, 1):
                    worksheet.column_dimensions[chr(64 + idx)].width = 20

            return caminho_completo
        except Exception as e:
            print(f"❌ Erro ao criar relatório: {e}")
            return None

    def enviar_email(self, arquivo_planilha, cnhs_vencendo):
        """
        Envia email com o relatório para o setor de frotas.

        Args:
            arquivo_planilha (str): Caminho do arquivo Excel a anexar
            cnhs_vencendo (pd.DataFrame): DataFrame com CNHs a alertar

        Returns:
            bool: True se email enviado com sucesso, False caso contrário
        """
        try:
            msg = MIMEMultipart('mixed')
            msg['Subject'] = f"🚨 Relatório de CNHs Vencendo - {datetime.now().strftime('%d/%m/%Y')}"
            msg['From'] = self.config.EMAIL_SENDER
            msg['To'] = self.config.EMAIL_DESTINATARIO
            msg['Date'] = formatdate(localtime=True)

            qtd = len(cnhs_vencendo)
            html = self._gerar_html_email(qtd, cnhs_vencendo)

            msg.attach(MIMEText(html, 'html'))

            if arquivo_planilha and os.path.exists(arquivo_planilha):
                self._anexar_arquivo(msg, arquivo_planilha)

            self._enviar_smtp(msg)
            print(f"✅ Email enviado com sucesso para {self.config.EMAIL_DESTINATARIO}")
            return True

        except smtplib.SMTPAuthenticationError:
            print("❌ Erro de autenticação. Verifique email e senha no .env")
            return False
        except Exception as e:
            print(f"❌ Erro ao enviar email: {e}")
            return False

    def _gerar_html_email(self, qtd, cnhs_vencendo):
        """Gera o HTML do email."""
        html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; color: #333;">
                <h2 style="color: #d9534f;">⚠️ Alerta de CNHs Vencendo</h2>
                <p>Olá,</p>
                <p>Foram encontradas <strong>{qtd} CNH(s)</strong> que vencem em até <strong>{self.config.DIAS_ALERTA} dias</strong>.</p>
                <p>Segue em anexo o relatório detalhado com os dados.</p>

                <h3>Resumo:</h3>
                <ul>
        """

        for _, row in cnhs_vencendo.iterrows():
            html += f"<li><strong>{row['Nome']}</strong> - CNH: {row['CNH']} - Vence em: {row['Validade']} ({row['Dias_para_vencer']} dias)</li>"

        html += """
                </ul>
                <p style="color: #666; font-size: 12px; margin-top: 20px;">
                    <em>Mensagem automática gerada pelo sistema de controle de CNH</em>
                </p>
            </body>
        </html>
        """
        return html

    def _anexar_arquivo(self, msg, arquivo_planilha):
        """Anexa o arquivo ao email."""
        with open(arquivo_planilha, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(arquivo_planilha)}'
            )
            msg.attach(part)

    def _enviar_smtp(self, msg):
        """Envia o email via SMTP."""
        with smtplib.SMTP(self.config.SMTP_SERVER, self.config.SMTP_PORT) as server:
            server.starttls()
            server.login(self.config.EMAIL_SENDER, self.config.EMAIL_PASSWORD)
            server.send_message(msg)

    def executar(self):
        """Executa a automação completa."""
        print(f"\n{'='*60}")
        print(f"🔍 Verificando CNHs - {obter_timestamp_legivel()}")
        print(f"{'='*60}\n")

        df = self.ler_arquivo_cnh()
        if df is None:
            return

        cnhs_vencendo = self.verificar_cnhs_vencendo(df)

        if len(cnhs_vencendo) > 0:
            print(f"⚠️  Encontradas {len(cnhs_vencendo)} CNH(s) vencendo em breve:")
            print(cnhs_vencendo[['Nome', 'CNH', 'Validade', 'Dias_para_vencer']].to_string(index=False))

            arquivo = self.criar_planilha_relatorio(cnhs_vencendo)
            if arquivo:
                print(f"\n📊 Planilha criada: {arquivo}")
                self.enviar_email(arquivo, cnhs_vencendo)
        else:
            print(f"✅ Nenhuma CNH vencendo nos próximos {self.config.DIAS_ALERTA} dias!")

        limpar_relatorios_antigos(self.config.PASTA_RELATORIOS, manter=10)
        print(f"\n{'='*60}\n")

    def agendar_execucao_diaria(self):
        """Agenda a execução diária em um horário específico."""
        schedule.every().day.at(self.config.HORARIO_EXECUCAO).do(self.executar)
        print(f"⏰ Automação agendada para executar diariamente às {self.config.HORARIO_EXECUCAO}")

        while True:
            schedule.run_pending()
            time.sleep(60)


def main():
    """Função principal."""
    print("""
    ╔════════════════════════════════════════════╗
    ║   AUTOMAÇÃO DE VERIFICAÇÃO DE CNH          ║
    ║   Sistema de Alerta de Vencimento          ║
    ╚════════════════════════════════════════════╝
    """)

    try:
        automacao = AutomacaoCNH()
        Config.exibir()
        automacao.agendar_execucao_diaria()
    except KeyboardInterrupt:
        print("\n\n❌ Automação interrompida pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro fatal: {e}")


if __name__ == '__main__':
    main()
