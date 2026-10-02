# 📧 Como Configurar o Email para a Automação

## 🎯 Objetivo
Você precisa configurar um arquivo `.env` com as credenciais de email para que o script possa enviar os alertas.

---

## ✅ OPÇÃO 1: Gmail (Recomendado)

### Passo 1: Ativar Verificação em Duas Etapas
1. Acesse: https://myaccount.google.com/security
2. Procure por **"Verificação em duas etapas"** (2-Step Verification)
3. Clique em **"Ativar"** e siga as instruções

### Passo 2: Gerar Senha de App
1. Acesse: https://myaccount.google.com/apppasswords
2. Você verá esta tela:
   ```
   Selecionar app: [Gmail ▼]
   Selecionar dispositivo: [Windows/Mac/Linux ▼]
   ```
3. Escolha **Gmail** no primeiro campo
4. Clique em **"Gerar"**
5. Google vai gerar uma senha de 16 caracteres
6. **Copie essa senha** (você usará no .env)

### Passo 3: Criar o arquivo .env

No PowerShell, na pasta do projeto:

```powershell
@"
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_SENDER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app_de_16_caracteres
EMAIL_DESTINATARIO=frotas@empresa.com.br
ARQUIVO_CNH=cnhs.xlsx
DIAS_ALERTA=7
"@ | Out-File .env -Encoding utf8
```

**Substitua:**
- `seu_email@gmail.com` → seu email Gmail
- `sua_senha_de_app_de_16_caracteres` → a senha gerada (sem espaços)
- `frotas@empresa.com.br` → email que receberá os alertas

---

## ✅ OPÇÃO 2: Outlook / Hotmail

### Configuração

```env
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
EMAIL_SENDER=seu_email@outlook.com
EMAIL_PASSWORD=sua_senha_normal
EMAIL_DESTINATARIO=frotas@empresa.com.br
ARQUIVO_CNH=cnhs.xlsx
DIAS_ALERTA=7
```

---

## ✅ OPÇÃO 3: Email Corporativo

Peça ao seu setor de TI:
- SMTP_SERVER (ex: mail.empresa.com.br)
- SMTP_PORT (geralmente 587 ou 465)
- Usuário e senha

Depois preencha no `.env`:
```env
SMTP_SERVER=mail.empresa.com.br
SMTP_PORT=587
EMAIL_SENDER=seu_usuario@empresa.com.br
EMAIL_PASSWORD=sua_senha
EMAIL_DESTINATARIO=frotas@empresa.com.br
ARQUIVO_CNH=cnhs.xlsx
DIAS_ALERTA=7
```

---

## 🧪 Testar a Configuração

Após criar o `.env`, execute:

```powershell
cd C:\Fontes\projetos\api-simples
& .\.venv\Scripts\Activate.ps1
python automacao_cnh.py
```

**Se funcionar, você verá:**
```
============================================================
🔍 Verificando CNHs - 02/10/2026 14:30:45
============================================================

⚠️  Encontradas 3 CNH(s) vencendo em breve:
      Nome Registro CNH   Validade Dias_para_vencer
João Silva  12345678900 05/10/2026                 3
Ana Costa   11122233344 04/10/2026                 2
Carlos Oliveira 55544433322 07/10/2026             5

📊 Planilha criada: relatorio_cnhs_vencendo_20261002_143045.xlsx
✅ Email enviado com sucesso para frotas@empresa.com.br

============================================================
```

---

## ❌ Solução de Problemas

### ❌ "Erro de autenticação"

**Gmail:**
- Verifique se a 2FA está ativada
- Use a senha de app (16 caracteres), não a senha normal
- Remova espaços da senha

**Outlook:**
- Use a senha normal do email
- Verifique SMTP_SERVER (smtp-mail.outlook.com)

**Corporativo:**
- Confirme com TI as credenciais
- Teste com outro cliente de email primeiro

### ❌ "Arquivo Excel não encontrado"

Certifique-se que está na pasta certa:
```powershell
# Deve estar aqui:
ls C:\Fontes\projetos\api-simples\cnhs.xlsx
```

### ❌ ".env não encontrado"

Verifique:
```powershell
# Criar o .env (se não existir)
if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "Arquivo .env criado - edite com suas credenciais!"
}
```

---

## 🔐 Segurança

⚠️ **IMPORTANTE:**
- O arquivo `.env` contém sua senha
- **NUNCA** commit no Git
- **NUNCA** compartilhe o arquivo `.env`
- Está no `.gitignore` por segurança

---

## 🚀 Próximo Passo

Após testar com sucesso, agende a automação:

```powershell
python agendar_tarefa_windows.py
# Escolha opção 1
```

Pronto! A automação rodará automaticamente todos os dias às 09:00 ⏰
