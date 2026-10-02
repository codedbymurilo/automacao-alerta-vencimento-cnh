# 🚗 Automação de Verificação de CNH

Sistema automático que verifica CNHs próximas de vencer e envia relatórios por email diariamente.

## 📋 Requisitos

- Python 3.8+
- Excel com dados de CNH
- Conta de email SMTP (Gmail recomendado)

---

## 🔧 Configuração Inicial

### 1️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2️⃣ Preparar o Arquivo Excel

Crie um arquivo `cnhs.xlsx` com a seguinte estrutura:

| Coluna A | Coluna B      | Coluna C   |
|----------|--------------|------------|
| Nome     | Registro CNH | Validade   |
| João Silva | 12345678900 | 15/12/2026 |
| Maria Santos | 98765432100 | 20/11/2026 |

**Formatação de datas:** DD/MM/YYYY

### 3️⃣ Configurar Variáveis de Ambiente

Copie o arquivo `.env.example` para `.env` e preencha os dados:

```bash
cp .env.example .env
```

Edite o arquivo `.env`:

```env
# Email SMTP Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_SENDER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_ou_app_password
EMAIL_DESTINATARIO=frotas@empresa.com.br

ARQUIVO_CNH=cnhs.xlsx
DIAS_ALERTA=7
```

#### 🔐 Configurando Gmail

**Se usar Gmail:**
1. Ative a verificação em 2 etapas: https://myaccount.google.com/security
2. Gere uma senha de app: https://myaccount.google.com/apppasswords
3. Use essa senha no `.env`

**Se usar outro email (ex: Outlook, corporativo):**
- SMTP_SERVER: smtp-mail.outlook.com (Outlook) ou smtp do seu domínio
- SMTP_PORT: 587 (TLS) ou 465 (SSL)
- EMAIL_PASSWORD: sua senha normal

---

## 🚀 Uso

### Execução Manual (Teste)

```bash
python automacao_cnh.py
```

A automação vai:
- ✅ Ler o arquivo Excel
- ✅ Verificar CNHs vencendo em 7 dias
- ✅ Criar relatório em Excel
- ✅ Enviar por email

### ⏰ Agendar Execução Diária

#### Opção 1: Windows Task Scheduler (Recomendado)

```bash
python agendar_tarefa_windows.py
```

Escolha a opção 1 e a tarefa será agendada para executar diariamente às 09:00.

**Para gerenciar:**
1. Abra `Task Scheduler`
2. Procure por `AutomacaoCNH`
3. Altere horário/frequência conforme necessário

#### Opção 2: Arquivo Batch para Iniciar Manualmente

Crie `iniciar_automacao.bat`:

```batch
@echo off
cd /d "%~dp0"
python automacao_cnh.py
pause
```

---

## 📊 Estrutura de Arquivos

```
projeto/
├── automacao_cnh.py          # Script principal
├── agendar_tarefa_windows.py # Agendador de tarefas
├── requirements.txt          # Dependências Python
├── .env                       # Variáveis de ambiente (NÃO VERSIONADO)
├── .env.example              # Template do .env
├── cnhs.xlsx                 # Arquivo com dados de CNH
├── relatorio_cnhs_vencendo_*.xlsx  # Relatórios gerados
└── SETUP.md                  # Este arquivo
```

---

## 🔍 Monitoramento

### Verificar Status da Tarefa (Windows)

```powershell
# Ver tarefas agendadas
schtasks /query /tn AutomacaoCNH

# Ver último resultado
schtasks /query /tn AutomacaoCNH /v

# Executar manualmente a tarefa
schtasks /run /tn AutomacaoCNH
```

### Logs

Os relatórios gerados ficam na mesma pasta com nome:
`relatorio_cnhs_vencendo_YYYYMMDD_HHMMSS.xlsx`

---

## ⚠️ Troubleshooting

### ❌ "Arquivo não encontrado"
- Certifique-se que `cnhs.xlsx` está na mesma pasta que `automacao_cnh.py`
- Verifique o nome do arquivo em `.env` (ARQUIVO_CNH)

### ❌ "Erro de autenticação ao enviar email"
- Verifique EMAIL_SENDER e EMAIL_PASSWORD em `.env`
- Se usar Gmail, gere uma senha de app (veja acima)
- Teste a conexão manualmente:
```python
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('seu_email@gmail.com', 'sua_senha')
```

### ❌ "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### ❌ "Tarefa não executa no horário"
1. Abra Task Scheduler
2. Localize `AutomacaoCNH`
3. Clique direito → Propriedades
4. Marque "Executar com privilégios mais altos"
5. Na aba "Disparadores", confirme o horário

---

## 📝 Personalizações

### Alterar Horário de Execução

Edite `automacao_cnh.py` (última linha):
```python
automacao.agendar_execucao_diaria(hora='14:30')  # Muda para 14:30
```

### Alterar Dias de Alerta

Em `.env`:
```env
DIAS_ALERTA=3  # Alerta com 3 dias de antecedência
```

### Múltiplos Destinatários

Em `.env`, adicione um por linha (adapte `automacao_cnh.py`):
```python
emails = os.getenv('EMAIL_DESTINATARIO').split(',')
```

---

## 🛡️ Segurança

⚠️ **IMPORTANTE:**
- Nunca commite o arquivo `.env` no git
- Adicione `.env` ao `.gitignore`
- Use senhas de app, não senhas reais (especialmente Gmail)
- O arquivo `.env` contém credenciais sensíveis

---

## 📞 Suporte

Se enfrentar problemas:
1. Verifique o `.env` está preenchido corretamente
2. Execute manualmente: `python automacao_cnh.py`
3. Veja as mensagens de erro
4. Teste a conexão SMTP com um script simples

---

**Versão:** 1.0  
**Última atualização:** 2026-10-02
