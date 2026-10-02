"""Configurações da automação de CNH."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Classe de configuração centralizada."""

    # Email SMTP
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
    EMAIL_SENDER = os.getenv('EMAIL_SENDER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    EMAIL_DESTINATARIO = os.getenv('EMAIL_DESTINATARIO')

    # Caminhos
    ARQUIVO_CNH = os.getenv('ARQUIVO_CNH', 'cnhs.xlsx')
    PASTA_RELATORIOS = os.getenv('PASTA_RELATORIOS', '').strip()

    # Configurações
    DIAS_ALERTA = int(os.getenv('DIAS_ALERTA', '7'))
    HORARIO_EXECUCAO = os.getenv('HORARIO_EXECUCAO', '09:00')

    @staticmethod
    def validar():
        """Valida as configurações essenciais."""
        erros = []

        if not Config.EMAIL_SENDER:
            erros.append("❌ EMAIL_SENDER não configurado no .env")
        if not Config.EMAIL_PASSWORD:
            erros.append("❌ EMAIL_PASSWORD não configurado no .env")
        if not Config.EMAIL_DESTINATARIO:
            erros.append("❌ EMAIL_DESTINATARIO não configurado no .env")
        if not Config.ARQUIVO_CNH:
            erros.append("❌ ARQUIVO_CNH não configurado no .env")

        return erros

    @staticmethod
    def exibir():
        """Exibe as configurações atuais."""
        print("\n📋 Configurações Atuais:")
        print(f"   📧 Email: {Config.EMAIL_SENDER}")
        print(f"   📂 Arquivo CNH: {Config.ARQUIVO_CNH}")
        print(f"   📁 Pasta Relatórios: {Config.PASTA_RELATORIOS or '(mesmo diretório do projeto)'}")
        print(f"   ⏰ Dias de Alerta: {Config.DIAS_ALERTA}")
        print(f"   🕐 Horário Execução: {Config.HORARIO_EXECUCAO}\n")
