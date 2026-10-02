# 🚗 Automação de Verificação de CNH - Documentação Técnica

## 📋 Visão Geral do Projeto

**Nome:** Automação de Verificação de CNH  
**Objetivo:** Automatizar verificação de CNHs próximas de vencer e alertar setor de frotas  
**Linguagem:** Python 3.8+  
**Status:** ✅ Produção  

---

## 🏗️ Arquitetura

### Camadas do Projeto

```
Entrada (Excel/Email) → Processamento (Automação) → Saída (Relatório/Email)
```

### Módulos Principais

**`src/config.py`**
- Gerencia todas as configurações
- Valida variáveis de ambiente
- Centraliza constantes

**`src/utils.py`**
- Funções utilitárias reutilizáveis
- Manipulação de caminhos
- Formatação de dados

**`src/automacao_cnh.py`**
- Classe principal `AutomacaoCNH`
- Orquestração do fluxo
- Lógica de negócio

**`run.py`**
- Entry point da aplicação
- Inicializa o ambiente

**`scripts/`**
- Scripts auxiliares independentes
- Agendamento de tarefas
- Geração de dados teste

---

## 🔄 Fluxo de Dados

```
┌─────────────────┐
│  arquivo .env   │ (variáveis de ambiente)
└────────┬────────┘
         │
         ↓
┌─────────────────┐      ┌──────────────────┐
│   Config        │─────→│  AutomacaoCNH    │
│  (validação)    │      │ (orquestração)   │
└─────────────────┘      └─────────┬────────┘
                                   │
                  ┌────────────────┼────────────────┐
                  │                │                │
                  ↓                ↓                ↓
         ┌─────────────────┐  ┌──────────┐  ┌──────────────┐
         │ Excel Input     │  │ Verificar│  │ Email Output │
         │ (cnhs.xlsx)     │  │ Datas    │  │ (relatório)  │
         └─────────────────┘  └──────────┘  └──────────────┘
```

---

## 📂 Estrutura de Arquivos

```
api-simples/
├── src/
│   ├── __init__.py              # Inicializador (exports)
│   ├── config.py                # Configurações
│   ├── utils.py                 # Utilitários
│   └── automacao_cnh.py         # Classe principal
│
├── scripts/
│   ├── agendar_tarefa_windows.py # Agendador
│   └── criar_excel_exemplo.py    # Gerador dados
│
├── docs/
│   ├── CONFIGURAR_EMAIL.md
│   ├── CONFIGURAR_CAMINHOS.md
│   ├── SETUP.md
│   └── INICIO_RAPIDO.md
│
├── example/
│   └── cnhs_exemplo.xlsx
│
├── tests/                       # Testes (futuros)
├── .env                         # Config (NUNCA VERSIONADO)
├── .env.example                 # Template config
├── run.py                       # Entry point
├── requirements.txt             # Dependências
├── README.md                    # Documentação pública
├── CLAUDE.md                    # Este arquivo
└── .gitignore
```

---

## 🔑 Classes e Métodos Principais

### `AutomacaoCNH`

```python
class AutomacaoCNH:
    def __init__()
        """Inicializa com config, prepara ambiente"""
    
    def ler_arquivo_cnh() → DataFrame
        """Lê Excel e normaliza colunas"""
    
    def verificar_cnhs_vencendo(df) → DataFrame
        """Filtra CNHs vencendo em DIAS_ALERTA"""
    
    def criar_planilha_relatorio(df) → str
        """Cria Excel formatado com alertas"""
    
    def enviar_email(arquivo, df) → bool
        """Envia email com relatório anexado"""
    
    def executar() → None
        """Orquestra todo o fluxo"""
    
    def agendar_execucao_diaria() → None
        """Loop infinito de agendamento"""
```

### `Config`

```python
class Config:
    # SMTP
    SMTP_SERVER: str
    SMTP_PORT: int
    EMAIL_SENDER: str
    EMAIL_PASSWORD: str
    EMAIL_DESTINATARIO: str
    
    # Caminhos
    ARQUIVO_CNH: str
    PASTA_RELATORIOS: str
    
    # Configuração
    DIAS_ALERTA: int
    HORARIO_EXECUCAO: str
    
    @staticmethod
    def validar() → List[str]
        """Retorna lista de erros (vazia = OK)"""
    
    @staticmethod
    def exibir() → None
        """Exibe configurações no terminal"""
```

---

## 🔧 Dependências

```
pandas==*          # Leitura/escrita Excel
openpyxl==*        # Formatação Excel
python-dotenv==*   # Carregamento .env
schedule==*        # Agendamento
```

Atualize com:
```bash
pip install -r requirements.txt --upgrade
```

---

## 💡 Decisões de Arquitetura

### 1. Por que usar `Config` como classe estática?

**Pro:** Centraliza todas as configurações, fácil validar, sem estado  
**Contra:** Não é testável com dependency injection  
**Alternativa rejeitada:** Singleton (mais complexo)

### 2. Por que separar `utils.py`?

**Pro:** Reutilizável, facilita testes, sem acoplamento  
**Alternativa rejeitada:** Métodos estáticos na classe principal (maior)

### 3. Por que usar `schedule` ao invés de `APScheduler`?

**Pro:** Simples, leve, sem dependências extras  
**Contra:** Menos recursos, sem persistência  
**Uso:** Desenvolvimento e produção pequeno. Para escala, considerar APScheduler

### 4. Por que Excel como formato entrada/saída?

**Pro:** Familiar para usuários não-técnicos, fácil editar  
**Contra:** Menos eficiente que banco de dados  
**Futura melhoria:** Suportar CSV, API, banco de dados

---

## 🧪 Testes (Estrutura)

```python
# tests/test_config.py
def test_config_validacao():
    """Valida se Config.validar() retorna erros corretos"""

# tests/test_automacao.py
def test_ler_arquivo_excel():
    """Valida leitura de Excel"""

def test_verificar_cnhs_vencendo():
    """Valida filtragem por data"""

def test_criar_planilha():
    """Valida criação do Excel"""

def test_formatar_email():
    """Valida geração do HTML do email"""
```

Executar testes:
```bash
pytest tests/ -v
```

---

## 🚀 Melhorias Futuras

### Curto Prazo
- [ ] Testes unitários (pytest)
- [ ] Logging estruturado (logging module)
- [ ] Suporte a múltiplos emails
- [ ] Relatório também em PDF

### Médio Prazo
- [ ] Banco de dados SQLite para histórico
- [ ] API REST para consultas
- [ ] Dashboard web (FastAPI + React)
- [ ] Suporte a CSV como entrada

### Longo Prazo
- [ ] Integração com sistemas de frota
- [ ] Machine learning para previsão
- [ ] App mobile para consultas
- [ ] Distribuição em múltiplas filiais

---

## 🔐 Considerações de Segurança

✅ **Implementado:**
- Credenciais em `.env` (não versionado)
- Validação de caminhos
- Tratamento de exceções
- Email com autenticação TLS

⚠️ **Não Implementado (Considerar):**
- Criptografia de .env
- Logs auditáveis
- Rate limiting
- Validação de entrada (DNI/CPF)

---

## 📊 Exemplo de Execução

```bash
$ python run.py

╔════════════════════════════════════════════╗
║   AUTOMAÇÃO DE VERIFICAÇÃO DE CNH          ║
║   Sistema de Alerta de Vencimento          ║
╚════════════════════════════════════════════╝

📋 Configurações Atuais:
   📧 Email: frotas@empresa.com.br
   📂 Arquivo CNH: cnhs.xlsx
   📁 Pasta Relatórios: (mesmo diretório do projeto)
   ⏰ Dias de Alerta: 7
   🕐 Horário Execução: 09:00

⏰ Automação agendada para executar diariamente às 09:00

[próxima execução aguardando...]
```

---

## 🐛 Debug e Logging

### Adicionar Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Iniciando automação")
logger.info("Email enviado com sucesso")
logger.warning("Pasta não encontrada, usando padrão")
logger.error("Erro ao ler Excel", exc_info=True)
```

### Debugar Configuração

```python
from src.config import Config
Config.exibir()  # Mostra todas as configurações
```

### Debugar Email

```python
import smtplib
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('user@gmail.com', 'password')
    print("✅ Email OK")
except Exception as e:
    print(f"❌ Erro: {e}")
```

---

## 📈 Performance

**Tempo de execução típico:**
- Ler Excel: 100-200ms
- Processar dados: 50-100ms
- Criar relatório: 200-300ms
- Enviar email: 500-2000ms (rede)

**Total:** ~1-3 segundos

**Otimizações possíveis:**
- Cache de leitura Excel
- Processamento paralelo
- Compressão de anexo

---

## 🔄 Versionamento

Seguir Semantic Versioning: `MAJOR.MINOR.PATCH`

- **MAJOR:** Mudanças incompatíveis (ex: novo arquivo obrigatório)
- **MINOR:** Novas features (ex: suporte a PDF)
- **PATCH:** Bug fixes (ex: correção de data)

Exemplo: `1.0.0` → `1.1.0` (nova feature)

---

## 📝 Convenções de Código

```python
# PEP 8 compliant
# - 80 caracteres max por linha
# - Nomes em snake_case (variáveis/funções)
# - Nomes em PascalCase (classes)
# - Docstrings em português

def funcao_exemplo(param1: str, param2: int) -> bool:
    """Descrição breve da função.
    
    Args:
        param1: Descrição do parâmetro
        param2: Descrição do parâmetro
    
    Returns:
        bool: Descrição do retorno
    """
    pass
```

---

## 🎓 Onboarding

Para novos colaboradores:

1. Clonar repositório
2. Ler este arquivo (CLAUDE.md)
3. Ler README.md
4. Configurar `.env` com dados teste
5. Executar `python run.py`
6. Explorar código em `src/`
7. Executar testes (quando implementados)

---

## 📞 Contato

- **Mantido por:** Murilo Neto
- **Email:** murilo.neto@montcalm.com.br
- **Última atualização:** Outubro 2026

---

## 📄 Licença

MIT License - Livre para usar, modificar e distribuir.

---

**Este documento deve ser atualizado quando:**
- Arquitetura mudar
- Novas dependências adicionadas
- Novos módulos criados
- Decisões importantes tomadas
