"""Funções utilitárias para a automação."""

import os
from datetime import datetime


def criar_pasta_se_nao_existir(caminho):
    """Cria uma pasta se ela não existir."""
    if caminho and not os.path.exists(caminho):
        try:
            os.makedirs(caminho, exist_ok=True)
            print(f"✅ Pasta criada: {caminho}")
            return True
        except Exception as e:
            print(f"⚠️  Aviso: Não foi possível criar pasta {caminho}: {e}")
            return False
    return True


def obter_caminho_relatorio(pasta_base, nome_arquivo):
    """Obtém o caminho completo do relatório."""
    if pasta_base:
        return os.path.join(pasta_base, nome_arquivo)
    return nome_arquivo


def gerar_nome_relatorio():
    """Gera um nome único para o relatório baseado no timestamp."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f'relatorio_cnhs_vencendo_{timestamp}.xlsx'


def validar_arquivo_existe(caminho):
    """Valida se um arquivo existe."""
    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        return False
    return True


def formatar_tabela_para_terminal(df):
    """Formata um DataFrame para exibição no terminal."""
    return df.to_string(index=False)


def obter_timestamp_legivel():
    """Retorna timestamp no formato legível."""
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')


def limpar_relatorios_antigos(pasta_relatorios, manter=10):
    """
    Remove relatórios antigos, mantendo apenas os N mais recentes.

    Args:
        pasta_relatorios (str): Caminho da pasta com relatórios
        manter (int): Quantidade de relatórios a manter (padrão 10)
    """
    if not pasta_relatorios or not os.path.exists(pasta_relatorios):
        return

    # Listar todos os arquivos .xlsx
    arquivos = [
        os.path.join(pasta_relatorios, f)
        for f in os.listdir(pasta_relatorios)
        if f.endswith('.xlsx')
    ]

    if len(arquivos) <= manter:
        return

    # Ordenar por data de modificação (mais antigos primeiro)
    arquivos.sort(key=os.path.getmtime)

    # Deletar os mais antigos
    deletados = 0
    for arquivo in arquivos[:-manter]:
        try:
            os.remove(arquivo)
            deletados += 1
        except Exception as e:
            print(f"⚠️  Erro ao deletar {os.path.basename(arquivo)}: {e}")

    if deletados > 0:
        print(f"🧹 Limpeza: {deletados} relatório(s) antigo(s) deletado(s)")
