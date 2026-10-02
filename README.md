# 🚗 Automação de Verificação de CNH

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#licença)

Sistema automático que verifica uma lista de CNHs em um arquivo Excel, identifica as que estão vencendo em breve e envia alertas por email para o setor de frotas.

**Status:** ✅ Pronto para produção

---

## 📋 Funcionalidades

✅ **Leitura de Excel** - Lê arquivo com dados de CNH (Nome, Registro, Validade)  
✅ **Verificação de Vencimento** - Detecta CNHs vencendo em até 7 dias (configurável)  
✅ **Relatório em Excel** - Gera planilha com CNHs próximas de vencer  
✅ **Alerta por Email** - Envia relatório para o setor de frotas  
✅ **Execução Automática** - Roda diariamente no horário configurado  
✅ **Configuração Flexível** - Suporta caminhos locais, UNC (rede) e variáveis de ambiente  

---

## 🏗️ Arquitetura do Projeto

```
projeto/
├── src/                          # Código principal
│   ├── __init__.py              # Inicializador do pacote
│   ├── automacao_cnh.py         # Classe principal (AutomacaoCNH)
│   ├── config.py                # Gerenciamento de configurações
│   └── utils.py                 # Funções utilitárias
│
├── scripts/                      # Scripts auxiliares
│   ├── agendar_tarefa_windows.py # Agendador de tarefas
│   └── criar_excel_exemplo.py    # Gerador de dados de teste
│
├── docs/                         # Documentação
│   ├── CONFIGURAR_EMAIL.md       # Guia: como configurar email
│   ├── CONFIGURAR_CAMINHOS.md    # Guia: caminhos de arquivo
│   ├── SETUP.md                  # Guia completo de setup
│   └── INICIO_RAPIDO.md          # Início rápido em 5 minutos
│
├── example/                      # Dados de exemplo
│   └── cnhs_exemplo.xlsx         # Excel com dados de teste
│
├── .env.example                  # Template de configuração
├── .env                          # Configurações (NÃO VERSIONADO)
├── run.py                        # Entry point principal
├── requirements.txt              # Dependências Python
├── README.md                     # Este arquivo
└── .gitignore                    # Configuração Git
```

---

## 🚀 Início Rápido (5 minutos)

### 1️⃣ Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes)
- Email SMTP configurado (Gmail, Outlook, etc)

### 2️⃣ Instalação

```bash
# Clonar ou baixar o projeto
cd c:\Fontes\projetos\api-simples

# Criar virtualenv (recomendado)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt
```

### 3️⃣ Configuração

```bash
# Copiar arquivo de template
copy .env.example .env

# Editar .env com suas credenciais
notepad .env
```

Preencha:
```env
EMAIL_SENDER=seu_email@gmail.com
EMAIL_PASSWORD=sua_app_password
EMAIL_DESTINATARIO=frotas@empresa.com.br
ARQUIVO_CNH=cnhs.xlsx
```

### 4️⃣ Testar

```bash
# Criar Excel com dados de teste
python scripts\criar_excel_exemplo.py

# Copiar para o mesmo diretório do projeto
copy example\cnhs_exemplo.xlsx cnhs.xlsx

# Executar automação
python run.py
```

### 5️⃣ Agendar (Automático)

```bash
# Agendar execução diária
python scripts\agendar_tarefa_windows.py
# Escolha opção 1
```

**Pronto!** 🎉 A automação está funcionando!

---

## 📚 Documentação Completa

Para configurações avançadas, veja:

| Documento | Descrição |
|-----------|-----------|
| [INICIO_RAPIDO.md](docs/INICIO_RAPIDO.md) | Guia 5 minutos para começar |
| [SETUP.md](docs/SETUP.md) | Guia completo de instalação |
| [CONFIGURAR_EMAIL.md](docs/CONFIGURAR_EMAIL.md) | Como configurar email SMTP |
| [CONFIGURAR_CAMINHOS.md](docs/CONFIGURAR_CAMINHOS.md) | Usar caminhos em servidor |

---

## ⚙️ Configuração Detalhada

### Variáveis de Ambiente (`.env`)

```env
# Email SMTP (obrigatório)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_SENDER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_app_password

# Email destinatário (obrigatório)
EMAIL_DESTINATARIO=frotas@empresa.com.br

# Caminhos dos arquivos (obrigatório)
ARQUIVO_CNH=cnhs.xlsx                    # Arquivo Excel com CNHs
PASTA_RELATORIOS=                        # Pasta dos relatórios (deixe em branco para projeto)

# Configuração de alerta
DIAS_ALERTA=7                            # Alertar CNHs vencendo em N dias
HORARIO_EXECUCAO=09:00                   # Horário da execução diária
```

### Exemplos de Caminhos

**Local (pasta do projeto):**
```env
ARQUIVO_CNH=cnhs.xlsx
PASTA_RELATORIOS=
```

**Caminho absoluto Windows:**
```env
ARQUIVO_CNH=C:\dados\cnhs.xlsx
PASTA_RELATORIOS=C:\dados\relatorios
```

**Servidor compartilhado (UNC):**
```env
ARQUIVO_CNH=\\servidor\compartilhamento\cnhs.xlsx
PASTA_RELATORIOS=\\servidor\compartilhamento\relatorios
```

---

## 📊 Estrutura do Excel

O arquivo `cnhs.xlsx` deve ter a seguinte estrutura:

| Coluna A | Coluna B | Coluna C |
|----------|----------|----------|
| Nome | Registro CNH | Validade |
| João Silva | 12345678900 | 15/12/2026 |
| Maria Santos | 98765432100 | 20/11/2026 |

**Formato de Data:** DD/MM/YYYY

---

## 📧 Configurando Email

### ✅ Gmail (Recomendado)

1. Ativar 2FA: https://myaccount.google.com/security
2. Gerar App Password: https://myaccount.google.com/apppasswords
3. Usar no `.env`:

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_SENDER=seu_email@gmail.com
EMAIL_PASSWORD=senha_de_16_caracteres_gerada
```

### ✅ Outlook

```env
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
EMAIL_SENDER=seu_email@outlook.com
EMAIL_PASSWORD=sua_senha_normal
```

### ✅ Email Corporativo

Peça as credenciais ao seu TI:

```env
SMTP_SERVER=mail.empresa.com.br
SMTP_PORT=587
EMAIL_SENDER=usuario@empresa.com.br
EMAIL_PASSWORD=sua_senha
```

Veja [CONFIGURAR_EMAIL.md](docs/CONFIGURAR_EMAIL.md) para mais detalhes.

---

## 🧪 Testando

### Teste Manual

```bash
# Ativar virtualenv
.\.venv\Scripts\Activate.ps1

# Executar manualmente
python run.py

# Executar teste rapido
python tests\agendar_rapido.py 10
```

Você deve ver:
- ✅ Arquivo Excel lido
- ✅ CNHs detectadas
- ✅ Planilha criada
- ✅ Email enviado

### Teste com Dados de Exemplo

```bash
# Criar Excel com dados de teste (vencem em 2-5 dias)
python scripts\criar_excel_exemplo.py

# Copiar para a pasta do projeto
copy example\cnhs_exemplo.xlsx cnhs.xlsx

# Executar
python run.py
```

### Teste de Email

```bash
python -c "
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('seu_email@gmail.com', 'sua_app_password')
print('✅ Email configurado corretamente!')
"
```

---

## 📅 Agendando Execução

### Windows Task Scheduler

```bash
# Abrir agendador
python scripts\agendar_tarefa_windows.py

# Escolher opção 1 e confirmar
```

A tarefa será criada como `AutomacaoCNH` e executará diariamente às 09:00.

**Gerenciar a tarefa:**
1. Abra **Task Scheduler** (Agendador de Tarefas)
2. Localize `AutomacaoCNH`
3. Clique direito → Propriedades para editar

**Verificar status:**
```bash
# Ver quando foi a última execução
schtasks /query /tn AutomacaoCNH /v

# Forçar execução agora
schtasks /run /tn AutomacaoCNH
```

---

## 🏃 Execução Contínua

Para manter a automação rodando 24/7:

### Opção 1: Windows Task Scheduler (Recomendado)

```bash
python scripts\agendar_tarefa_windows.py
```

A tarefa executará todos os dias na hora configurada.

### Opção 2: Script Batch Contínuo

Crie `iniciar_automacao_24h.bat`:

```batch
@echo off
:loop
python run.py
timeout /t 86400 /nobreak
goto loop
```

Execute e deixe aberto na área de trabalho.

---

## 📦 Dependências

- **pandas** - Leitura e manipulação de Excel
- **openpyxl** - Escrita formatada em Excel
- **python-dotenv** - Carregamento de variáveis de ambiente
- **schedule** - Agendamento de tarefas

Instale com:
```bash
pip install -r requirements.txt
```

---

## 🔐 Segurança

⚠️ **IMPORTANTE:**

- ✅ O arquivo `.env` contém sua senha
- ✅ Nunca commit no Git (está em `.gitignore`)
- ✅ Nunca compartilhe o arquivo `.env`
- ✅ Use App Passwords em vez de senha real (Gmail)
- ✅ Revise o email gerado antes de enviar (production)

---

## 📈 Fluxo de Execução

```
1. Carrega configurações do .env
   ↓
2. Valida credenciais necessárias
   ↓
3. Lê arquivo Excel com CNHs
   ↓
4. Verifica CNHs vencendo em 7 dias
   ↓
5. Se encontrou alertas:
   ├→ Cria relatório em Excel
   ├→ Formata email HTML
   ├→ Anexa planilha
   └→ Envia para setor de frotas
   ↓
6. Próxima execução em 24h (se agendado)
```

---

## 🎯 Casos de Uso

### Cenário 1: Desenvolvimento Local

```env
ARQUIVO_CNH=cnhs.xlsx
PASTA_RELATORIOS=
EMAIL_DESTINATARIO=seu_email@teste.com
```

### Cenário 2: Produção Centralizada

```env
ARQUIVO_CNH=\\servidor-frotas\dados\cnhs.xlsx
PASTA_RELATORIOS=\\servidor-frotas\relatorios
EMAIL_DESTINATARIO=frotas@empresa.com.br
DIAS_ALERTA=7
```

### Cenário 3: Múltiplos Servidores

Crie `.env.prod` com credenciais de produção:
```bash
# Usar arquivo específico (edite src/config.py se necessário)
python run.py
```

---

## 🤝 Contribuindo

Para melhorias ou correções:

1. Teste suas mudanças localmente
2. Verifique se não quebrou funcionalidades existentes
3. Documente as mudanças

---

## 📄 Licença

MIT License - Veja detalhes em LICENSE

---

## 🎉 Versão

- **Versão:** 1.0.0
- **Última atualização:** Outubro 2026
- **Status:** ✅ Produção

