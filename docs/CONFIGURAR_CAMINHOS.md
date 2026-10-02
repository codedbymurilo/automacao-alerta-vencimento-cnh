# 📁 Configurar Caminhos de Arquivos para Produção

Por padrão, a automação salva os relatórios na mesma pasta do projeto. Você pode mudar isso para qualquer lugar do seu sistema.

---

## 🎯 Variáveis no `.env`

```env
# Arquivo Excel com dados de CNH
ARQUIVO_CNH=cnhs.xlsx

# Pasta onde salvar os relatórios (deixe em branco para usar a pasta do projeto)
PASTA_RELATORIOS=
```

---

## 📋 Exemplos de Configuração

### ✅ Opção 1: Pasta Local do Projeto (Padrão)

```env
ARQUIVO_CNH=cnhs.xlsx
PASTA_RELATORIOS=
```

**Resultado:**
- Lê: `C:\Fontes\projetos\api-simples\cnhs.xlsx`
- Salva: `C:\Fontes\projetos\api-simples\relatorio_cnhs_vencendo_*.xlsx`

---

### ✅ Opção 2: Caminho Absoluto no Windows

```env
ARQUIVO_CNH=C:\dados\cnhs.xlsx
PASTA_RELATORIOS=C:\dados\relatorios
```

**Resultado:**
- Lê: `C:\dados\cnhs.xlsx`
- Salva: `C:\dados\relatorios\relatorio_cnhs_vencendo_*.xlsx`

---

### ✅ Opção 3: Pasta Compartilhada na Rede (UNC Path)

```env
ARQUIVO_CNH=\\servidor\compartilhamento\cnhs.xlsx
PASTA_RELATORIOS=\\servidor\compartilhamento\relatorios
```

**Resultado:**
- Lê: `\\servidor\compartilhamento\cnhs.xlsx`
- Salva: `\\servidor\compartilhamento\relatorios\relatorio_cnhs_vencendo_*.xlsx`

---

### ✅ Opção 4: Usar Variáveis de Ambiente do Windows

Se preferir, pode usar variáveis de ambiente do Windows:

```env
ARQUIVO_CNH=%USERPROFILE%\Documents\cnhs.xlsx
PASTA_RELATORIOS=%USERPROFILE%\Documents\relatorios_cnh
```

---

## 🔧 Casos de Uso Comuns

### Cenário 1: Arquivo em Pasta Compartilhada, Relatórios Locais

```env
# Arquivo Excel está em servidor de rede
ARQUIVO_CNH=\\servidor-frotas\compartilhado\cnhs.xlsx

# Relatórios salvos localmente para análise
PASTA_RELATORIOS=C:\relatorios_cnh
```

---

### Cenário 2: Tudo Centralizado em Servidor

```env
# Tudo em um único lugar centralizado
ARQUIVO_CNH=\\servidor-frotas\compartilhado\dados\cnhs.xlsx
PASTA_RELATORIOS=\\servidor-frotas\compartilhado\relatorios
```

---

### Cenário 3: Desenvolvimento vs Produção

**Arquivo `.env.dev` (desenvolvimento):**
```env
ARQUIVO_CNH=cnhs.xlsx
PASTA_RELATORIOS=
```

**Arquivo `.env.prod` (produção):**
```env
ARQUIVO_CNH=\\servidor-produção\frotas\cnhs.xlsx
PASTA_RELATORIOS=\\servidor-produção\frotas\relatorios
```

Depois execute com:
```powershell
python automacao_cnh.py  # Usa .env por padrão
```

---

## ⚙️ Dicas Importantes

### 1️⃣ Caminhos com Espaços

Se o caminho tem espaços, isso funcionará normalmente:

```env
ARQUIVO_CNH=C:\Dados da Empresa\CNH\cnhs.xlsx
PASTA_RELATORIOS=C:\Relatórios\CNH Vencendo
```

### 2️⃣ Criar a Pasta Automaticamente

Se `PASTA_RELATORIOS` não existir, a automação cria automaticamente:

```python
✅ Pasta de relatórios criada: C:\dados\relatorios
```

### 3️⃣ Permissões de Acesso

Certifique-se que:
- ✅ O usuário tem permissão de **leitura** em `ARQUIVO_CNH`
- ✅ O usuário tem permissão de **escrita** em `PASTA_RELATORIOS`
- ✅ Para pastas de rede, verificar credenciais

### 4️⃣ Verificar o Caminho

Você pode testar o acesso antes de configurar:

```powershell
# Testar se consegue ler o arquivo
Test-Path "C:\dados\cnhs.xlsx"  # Deve retornar True

# Testar se consegue escrever
"teste" | Out-File "C:\dados\relatorios\teste.txt"
Remove-Item "C:\dados\relatorios\teste.txt"
```

---

## 🧪 Teste de Configuração

Após configurar os caminhos, execute:

```powershell
cd C:\Fontes\projetos\api-simples
& .\.venv\Scripts\Activate.ps1

# Teste manual
python automacao_cnh.py
```

Verifique:
- ✅ Arquivo Excel lido com sucesso
- ✅ Relatório criado em `PASTA_RELATORIOS`
- ✅ Email enviado

---

## ❌ Troubleshooting

### ❌ "Arquivo não encontrado"

```
❌ Arquivo C:\dados\cnhs.xlsx não encontrado!
```

**Solução:**
1. Verifique se o caminho está correto
2. Confirme as permissões de acesso
3. Teste com: `Test-Path "C:\dados\cnhs.xlsx"`

### ❌ "Permissão negada ao salvar relatório"

```
❌ Erro ao salvar: Permission denied
```

**Solução:**
1. Verifique permissões de escrita na pasta
2. Teste criar um arquivo manualmente na pasta
3. Verifique se o antivírus está bloqueando

### ❌ "Caminho de rede inacessível"

```
❌ Arquivo \\servidor\compartilhamento\cnhs.xlsx não encontrado!
```

**Solução:**
1. Verifique se a rede está acessível: `Test-Path "\\servidor\compartilhamento"`
2. Verifique credenciais de rede
3. Teste manualmente: `Copy-Item "\\servidor\compartilhamento\teste.txt" .`

---

## 📝 Exemplo Completo para Produção

```env
# ========== PRODUÇÃO ==========

# Email SMTP Configuration
SMTP_SERVER=smtp.empresa.com.br
SMTP_PORT=587
EMAIL_SENDER=automacao@empresa.com.br
EMAIL_PASSWORD=senha_corporativa

# Destinatários
EMAIL_DESTINATARIO=frotas@empresa.com.br

# Caminhos em servidor compartilhado
ARQUIVO_CNH=\\servidor-empresa\departamentos\frotas\cnhs.xlsx
PASTA_RELATORIOS=\\servidor-empresa\departamentos\frotas\alertas_cnh

# Configuração
DIAS_ALERTA=7
```

---

## ✅ Checklist de Produção

- [ ] `ARQUIVO_CNH` aponta para o Excel correto
- [ ] `PASTA_RELATORIOS` aponta para pasta com permissões de escrita
- [ ] Testou acessar manualmente ambas as pastas
- [ ] Antivírus não está bloqueando os caminhos
- [ ] Executou `python automacao_cnh.py` com sucesso
- [ ] Relatório foi criado na pasta correta
- [ ] Email foi enviado

Pronto! Sua automação agora está configurada para produção! 🚀
