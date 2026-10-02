"""
Script rápido para testar a automação sem aguardar agendamento
"""

import sys
import os

# Mudar para a raiz do projeto (para arquivos relativos funcionarem)
os.chdir(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from automacao_cnh import AutomacaoCNH

if __name__ == '__main__':
    print("""
    ╔════════════════════════════════════════════╗
    ║   TESTE DE AUTOMAÇÃO DE CNH                ║
    ║   (Execução Única - Sem Agendamento)       ║
    ╚════════════════════════════════════════════╝
    """)

    try:
        automacao = AutomacaoCNH()
        automacao.executar()
    except KeyboardInterrupt:
        print("\n❌ Teste interrompido")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
