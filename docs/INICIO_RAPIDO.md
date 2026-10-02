# ⚡ Guia de Início Rápido

Siga estes passos para testar a automação em 5 minutos:

## 1️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

## 2️⃣ Criar Arquivo Excel de Teste

```bash
python criar_excel_exemplo.py
```

Isso cria um arquivo `cnhs.xlsx` com 5 registros de teste (alguns vencem em 2-5 dias).

## 3️⃣ Configurar Email (.env)

Copie o arquivo de template:
```bash
cp .env.example .env
```

Edite `.env` e preencha:
- `EMAIL_SENDER`: seu email
- `EMAIL_PASSWORD`: sua senha ou app password
- `EMAIL_DESTINATARIO`: para onde enviar os alertas

**Gmail?**
1. Ativa 2FA: https://myaccount.google.com/security
2. Gera senha de app: https://myaccount.google.com/apppasswords
3. Coloca no `.env`

## 4️⃣ Testar Execução

```bash
python automacao_cnh.py
```

Você deve ver:
- ✅ Arquivo lido com sucesso
- ✅ CNHs próximas de vencer identificadas
- ✅ Planilha `relatorio_cnhs_vencendo_*.xlsx` criada
- ✅ Email enviado para `EMAIL_DESTINATARIO`

## 5️⃣ Agendar Execução Diária

```bash
python agendar_tarefa_windows.py
```

Escolha opção `1` para agendar a execução automática diariamente às 09:00.

---

## ✅ Checklist de Configuração

- [ ] `requirements.txt` - dependências instaladas
- [ ] `cnhs.xlsx` - arquivo Excel criado/preparado
- [ ] `.env` - configurado com credenciais
- [ ] Teste manual - `python automacao_cnh.py` executado com sucesso
- [ ] Tarefa agendada - `python agendar_tarefa_windows.py` executado
- [ ] Email recebido - verificou inbox para teste de email

---

## 🐛 Deu Erro?

### Erro de módulo/dependência
```bash
pip install -r requirements.txt --upgrade
```

### Erro de autenticação SMTP
- Verifique EMAIL_SENDER e EMAIL_PASSWORD
- Se Gmail, confirme que gerou app password (não senha normal)
- Teste com:
```python
import smtplib
smtplib.SMTP('smtp.gmail.com', 587).starttls()
```

### Arquivo Excel não encontrado
- Certifique-se que `cnhs.xlsx` está na mesma pasta
- Verifique o nome em `.env` (ARQUIVO_CNH=)

### Tarefa não executa
- Execute como Administrador
- Abra Task Scheduler e confirme a tarefa `AutomacaoCNH`

---

## 📖 Próximos Passos

Após confirmar que funciona:

1. **Substitua o Excel de teste**: Troque `cnhs.xlsx` com seus dados reais
2. **Customize o horário**: Edite `automacao_cnh.py` última linha (hora='09:00')
3. **Customize os dias**: Altere `DIAS_ALERTA=7` em `.env`
4. **Adicione múltiplos emails**: Edite `automacao_cnh.py` para suportar

---

## 🚀 Tudo Pronto!

A automação agora está:
- ✅ Executando diariamente
- ✅ Verificando CNHs que vencem em 7 dias
- ✅ Criando relatórios em Excel
- ✅ Enviando para o email do setor de frotas

**Nenhuma ação manual necessária!** 🎉

---

Para configurações avançadas, veja `SETUP.md`
