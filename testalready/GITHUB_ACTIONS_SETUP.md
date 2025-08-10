# 🚀 Configuração do GitHub Actions

Este guia explica como configurar e usar o GitHub Actions para executar os testes automaticamente.

## 📋 Pré-requisitos

- ✅ Projeto hospedado no GitHub
- ✅ Acesso de administrador ao repositório
- ✅ GitHub Actions habilitado (padrão em repositórios públicos)

## 🔧 Configuração Automática

### 1. Estrutura de Arquivos
O projeto já inclui todos os arquivos necessários:

```
.github/
├── workflows/
│   ├── ci.yml              # Workflow principal de testes
│   └── badge.yml           # Geração de badges (opcional)
.codecov.yml                 # Configuração do Codecov
```

### 2. Ativar GitHub Actions
1. **Faça push** dos arquivos para o GitHub
2. **Acesse a aba "Actions"** no repositório
3. **GitHub Actions será ativado automaticamente**

## 🧪 Como Funciona

### Workflow Principal (`ci.yml`)
O workflow executa **3 jobs paralelos**:

1. **🐍 Testes Backend (Django)**
   - Python 3.12 + pipenv
   - Instala dependências
   - Executa migrações
   - Roda testes com pytest
   - Gera relatório de cobertura

2. **⚛️ Testes Frontend (React)**
   - Node.js 18 + npm
   - Instala dependências
   - Executa testes com Vitest
   - Gera relatório de cobertura

3. **🚀 Testes Completos**
   - Depende dos jobs anteriores
   - Executa o script principal
   - Validação completa do projeto

### Triggers
- ✅ **Push** para `main`, `master`, `develop`
- ✅ **Pull Request** para qualquer branch
- ✅ **Manual** (via GitHub UI)

## 📊 Relatórios e Cobertura

### GitHub Actions
- **Logs detalhados** de cada job
- **Status visual** (✅/❌) para cada etapa
- **Tempo de execução** de cada job
- **Artefatos** para download

### Codecov (Opcional)
Para relatórios de cobertura online:

1. **Conecte ao Codecov**:
   - Acesse: https://codecov.io/
   - Conecte com GitHub
   - Selecione o repositório

2. **Configure o token**:
   - Vá em Settings > Repository Upload Token
   - Copie o token

3. **Adicione o secret**:
   - GitHub > Settings > Secrets and variables > Actions
   - Crie: `CODECOV_TOKEN`
   - Cole o token do Codecov

## 🎯 Uso para Avaliadores

### Opção 1: Execução Automática
1. **Clone o repositório**
2. **Faça qualquer alteração** (ex: adicione um comentário)
3. **Faça push** para qualquer branch
4. **Acesse Actions** para ver os resultados

### Opção 2: Pull Request
1. **Fork o repositório**
2. **Crie uma branch** com suas alterações
3. **Abra um Pull Request**
4. **GitHub Actions executará automaticamente**

### Opção 3: Execução Manual
1. **Acesse a aba Actions**
2. **Clique em "Run workflow"**
3. **Selecione a branch**
4. **Clique em "Run workflow"**

## 📱 Monitoramento

### Dashboard do GitHub Actions
- **Visão geral** de todos os workflows
- **Histórico** de execuções
- **Status** de cada job
- **Logs** detalhados de erro

### Notificações
- **Email** quando workflows falham
- **Status checks** em Pull Requests
- **Badges** de status (se configurado)

## 🔍 Solução de Problemas

### Workflow Falhando
1. **Verifique os logs** clicando no job falhado
2. **Identifique o erro** específico
3. **Corrija o problema** no código
4. **Faça push** para executar novamente

### Dependências Falhando
- **Python**: Verifique versão (3.12+)
- **Node.js**: Verifique versão (18+)
- **Cache**: Limpe cache do GitHub Actions

### Tempo de Execução
- **Backend**: ~2-3 minutos
- **Frontend**: ~1-2 minutos
- **Total**: ~3-5 minutos

## 🎉 Benefícios

### Para Avaliadores
- ⚡ **Execução mais rápida** (paralela)
- 🔄 **Automático** a cada alteração
- 📊 **Relatórios online** de cobertura
- 🚫 **Não precisa instalar** nada
- 📱 **Acesso de qualquer lugar**

### Para Desenvolvedores
- 🚨 **Detecção precoce** de problemas
- 📈 **Histórico** de qualidade do código
- 🔒 **Proteção** de branches principais
- 📊 **Métricas** de cobertura contínuas

## 📚 Recursos Adicionais

### Documentação Oficial
- [GitHub Actions](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Python Setup](https://github.com/actions/setup-python)
- [Node.js Setup](https://github.com/actions/setup-node)

### Exemplos e Templates
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [Python Testing](https://github.com/actions/setup-python#examples)
- [React Testing](https://github.com/actions/setup-node#examples)

---

**🚀 Com o GitHub Actions configurado, os testes serão executados automaticamente a cada alteração!**
