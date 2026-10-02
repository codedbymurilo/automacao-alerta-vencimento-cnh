"""
Script para criar um arquivo Excel de exemplo para testes.

Execute:
    python scripts/criar_excel_exemplo.py
"""

import pandas as pd
from datetime import datetime, timedelta
import os


def criar_excel_exemplo(caminho='example/cnhs_exemplo.xlsx'):
    """Cria um arquivo Excel com dados de exemplo."""
    # Dados de exemplo com datas próximas de vencer
    dados = {
        'Nome': [
            'João Silva',
            'Maria Santos',
            'Carlos Oliveira',
            'Ana Costa',
            'Pedro Ferreira'
        ],
        'Registro CNH': [
            '12345678900',
            '98765432100',
            '55544433322',
            '11122233344',
            '99988877766'
        ],
        'Validade': [
            (datetime.now() + timedelta(days=3)).strftime('%d/%m/%Y'),    # Vence em 3 dias ⚠️
            (datetime.now() + timedelta(days=8)).strftime('%d/%m/%Y'),    # Vence em 8 dias
            (datetime.now() + timedelta(days=5)).strftime('%d/%m/%Y'),    # Vence em 5 dias ⚠️
            (datetime.now() + timedelta(days=2)).strftime('%d/%m/%Y'),    # Vence em 2 dias ⚠️
            (datetime.now() + timedelta(days=15)).strftime('%d/%m/%Y'),   # Vence em 15 dias
        ]
    }

    # Criar pasta example se não existir
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    # Criar DataFrame e salvar
    df = pd.DataFrame(dados)
    df.to_excel(caminho, index=False, sheet_name='CNHs')

    print(f'✅ Arquivo {caminho} criado com sucesso!')
    print('\n📊 Dados de exemplo criados:')
    print(df.to_string(index=False))
    print('\n⚠️  Os primeiros 3 registros vencem em 2-5 dias e devem gerar alertas!')
    print(f'\n💡 Dica: Copie este arquivo para {os.path.join(os.path.dirname(__file__), "..", "cnhs.xlsx")} para testar')


if __name__ == '__main__':
    criar_excel_exemplo()
