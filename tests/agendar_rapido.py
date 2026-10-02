"""
Script para teste RÁPIDO com contagem de segundos (sem aguardar muito).

Uso:
    python tests\agendar_rapido.py        (executa em 30s padrão)
    python tests\agendar_rapido.py 60     (executa em 60s)
    python tests\agendar_rapido.py 90     (executa em 90s)
    python tests\agendar_rapido.py 0      (executa já)
"""

import sys
import os
import time
from datetime import datetime, timedelta

# Mudar para a raiz do projeto (para arquivos relativos funcionarem)
os.chdir(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from automacao_cnh import AutomacaoCNH


def main():
    print("""
    ╔════════════════════════════════════════════╗
    ║   TESTE RÁPIDO DE AGENDAMENTO              ║
    ║   Executa em X segundos                    ║
    ╚════════════════════════════════════════════╝
    """)

    try:
        # Lê segundos do parâmetro (padrão 30s)
        segundos = int(sys.argv[1]) if len(sys.argv) > 1 else 30

        if segundos < 0:
            print("❌ Segundos não pode ser negativo")
            sys.exit(1)

        automacao = AutomacaoCNH()

        agora = datetime.now()
        execucao_em = agora + timedelta(seconds=segundos)

        print(f"⏰ Hora Atual: {agora.strftime('%H:%M:%S')}")
        print(f"🕐 Execução em: {execucao_em.strftime('%H:%M:%S')}")
        print(f"⏳ Aguardando {segundos} segundos...\n")

        # Aguarda e mostra countdown
        for i in range(segundos, 0, -1):
            print(f"   {i}s", end='\r')
            time.sleep(1)

        print(f"\n✅ Executando automação agora!\n")
        automacao.executar()

    except ValueError:
        print("❌ Parâmetro inválido. Use um número de segundos.")
        print("   Uso: python tests\\agendar_rapido.py [segundos]")
        print("   Exemplos:")
        print("      python tests\\agendar_rapido.py 30")
        print("      python tests\\agendar_rapido.py 60")
        print("      python tests\\agendar_rapido.py 90")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n❌ Teste interrompido")
    except Exception as e:
        print(f"\n❌ Erro: {e}")


if __name__ == '__main__':
    main()
