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
