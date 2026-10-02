# Script para iniciar a automação facilmente
# Execute: .\scripts\iniciar.ps1

Write-Host @"
╔════════════════════════════════════════════╗
║   AUTOMAÇÃO DE VERIFICAÇÃO DE CNH          ║
║   Iniciador Rápido                         ║
╚════════════════════════════════════════════╝
"@

# Verificar se .venv existe
if (-not (Test-Path .\.venv)) {
    Write-Host "❌ Virtualenv não encontrado!"
    Write-Host "📝 Criando virtualenv..."
    python -m venv .venv
}

# Ativar virtualenv
Write-Host "✅ Ativando virtualenv..."
& .\.venv\Scripts\Activate.ps1

# Verificar dependências
Write-Host "📦 Verificando dependências..."
pip list | Select-String "pandas" | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Dependências não encontradas. Instalando..."
    pip install -r requirements.txt
}

# Verificar se .env existe
if (-not (Test-Path .\.env)) {
    Write-Host "`n⚠️  Arquivo .env não encontrado!"
    Write-Host "📝 Criando .env a partir de .env.example..."
    Copy-Item .env.example .env
    Write-Host "`n✏️  EDITE o arquivo .env com suas credenciais:"
    Write-Host "   notepad .env`n"
}

# Verificar se cnhs.xlsx existe
if (-not (Test-Path cnhs.xlsx)) {
    Write-Host "`n⚠️  Arquivo cnhs.xlsx não encontrado!"
    Write-Host "📝 Criando dados de exemplo..."
    python scripts\criar_excel_exemplo.py
    Copy-Item example\cnhs_exemplo.xlsx cnhs.xlsx
    Write-Host "`n✅ Arquivo cnhs.xlsx criado com dados de teste"
}

# Mostrar menu de opções
Write-Host "`n┌────────────────────────────────────┐"
Write-Host "│  O que deseja fazer?               │"
Write-Host "├────────────────────────────────────┤"
Write-Host "│  1 - Executar automação agora      │"
Write-Host "│  2 - Editar .env                   │"
Write-Host "│  3 - Agendar execução diária       │"
Write-Host "│  4 - Visualizar configuração       │"
Write-Host "│  0 - Sair                          │"
Write-Host "└────────────────────────────────────┘"

$opcao = Read-Host "`nEscolha (0-4)"

switch ($opcao) {
    "1" {
        Write-Host "`n🚀 Executando automação...$n"
        python run.py
    }
    "2" {
        Write-Host "`n📝 Abrindo .env..."
        notepad .env
    }
    "3" {
        Write-Host "`n⏰ Agendando..."
        python scripts\agendar_tarefa_windows.py
    }
    "4" {
        Write-Host "`n📋 Configuração:"
        python -c "
import sys
sys.path.insert(0, 'src')
from config import Config
Config.exibir()
"
    }
    "0" {
        Write-Host "`nSaindo..."
        exit
    }
    default {
        Write-Host "❌ Opção inválida!"
    }
}
