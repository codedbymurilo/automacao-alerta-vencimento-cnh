"""
Agendador de Tarefas do Windows - Task Scheduler

Script para criar/remover uma tarefa agendada no Windows que executa
a automação de CNH diariamente.

Execute como administrador:
    python scripts/agendar_tarefa_windows.py
"""

import subprocess
import os
import sys
from pathlib import Path


class AgendadorTarefas:
    """Gerencia agendamento de tarefas no Windows Task Scheduler."""

    NOME_TAREFA = 'AutomacaoCNH'
    HORARIO_PADRAO = '09:00'

    @staticmethod
    def criar_tarefa_agendada(horario=HORARIO_PADRAO):
        """Cria uma tarefa agendada no Windows."""
        script_path = Path(__file__).parent.parent / 'run.py'
        python_exe = sys.executable

        comando = (
            f'schtasks /create /tn "{AgendadorTarefas.NOME_TAREFA}" '
            f'/tr "{python_exe} \'{script_path}\'" '
            f'/sc daily /st {horario} /f'
        )

        try:
            print("🔧 Criando tarefa agendada no Windows...")
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

            if resultado.returncode == 0:
                print(f"✅ Tarefa '{AgendadorTarefas.NOME_TAREFA}' criada com sucesso!")
                print(f"⏰ Será executada diariamente às {horario}")
                print("\n📋 Para gerenciar:")
                print("   - Abra: Task Scheduler")
                print(f"   - Procure por: {AgendadorTarefas.NOME_TAREFA}")
                print("   - Clique direito para editar propriedades")
            else:
                print(f"❌ Erro ao criar tarefa: {resultado.stderr}")
                if "acesso negado" in resultado.stderr.lower():
                    print("\n⚠️  Certifique-se de executar como Administrador!")

        except Exception as e:
            print(f"❌ Erro: {e}")

    @staticmethod
    def remover_tarefa_agendada():
        """Remove a tarefa agendada."""
        comando = f'schtasks /delete /tn "{AgendadorTarefas.NOME_TAREFA}" /f'

        try:
            print(f"🗑️  Removendo tarefa '{AgendadorTarefas.NOME_TAREFA}'...")
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

            if resultado.returncode == 0:
                print(f"✅ Tarefa removida com sucesso!")
            else:
                print(f"❌ Erro: {resultado.stderr}")
        except Exception as e:
            print(f"❌ Erro: {e}")

    @staticmethod
    def listar_tarefas():
        """Lista a tarefa agendada."""
        comando = f'schtasks /query /tn "{AgendadorTarefas.NOME_TAREFA}" /v'

        try:
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            if resultado.returncode == 0:
                print(f"✅ Tarefa encontrada:\n{resultado.stdout}")
            else:
                print(f"⚠️  Tarefa não encontrada ou erro: {resultado.stderr}")
        except Exception as e:
            print(f"❌ Erro: {e}")


def main():
    """Menu principal."""
    print("""
    ╔════════════════════════════════════════════╗
    ║   AGENDADOR DE TAREFAS - WINDOWS           ║
    ║   Automação de CNH                         ║
    ╚════════════════════════════════════════════╝
    """)

    print("Opções:")
    print("1 - Criar tarefa agendada")
    print("2 - Remover tarefa agendada")
    print("3 - Listar status da tarefa")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção (0-3): ").strip()

    if opcao == '1':
        horario = input("Horário de execução (padrão 09:00): ").strip() or AgendadorTarefas.HORARIO_PADRAO
        AgendadorTarefas.criar_tarefa_agendada(horario)
    elif opcao == '2':
        AgendadorTarefas.remover_tarefa_agendada()
    elif opcao == '3':
        AgendadorTarefas.listar_tarefas()
    elif opcao == '0':
        print("Saindo...")
    else:
        print("❌ Opção inválida!")


if __name__ == '__main__':
    main()
