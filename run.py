"""
Entry point principal da Automação de CNH.

Execute para iniciar a automação:
    python run.py
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from automacao_cnh import main


if __name__ == '__main__':
    main()
