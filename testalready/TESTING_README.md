# 🧪 Guia de Execução de Testes

Este documento explica como executar todos os testes do projeto de forma fácil e rápida.

## 📋 Pré-requisitos

### Para o Backend (Django)
- Python 3.12+
- pipenv instalado (`pip install pipenv`)

### Para o Frontend (React)
- Node.js 18+
- npm

## 🚀 Execução Rápida (Recomendado)

### Opção 1: GitHub Actions (Mais Rápido - Automatizado)
Se o projeto estiver no GitHub, os testes são executados automaticamente:

1. **Faça push para qualquer branch** ou **abra um Pull Request**
2. **Acesse a aba "Actions"** no GitHub
3. **Veja os resultados em tempo real** dos testes
4. **Relatórios de cobertura** são gerados automaticamente

✅ **Vantagens:**
- ⚡ Execução mais rápida (paralela)
- 🔄 Automatizado a cada push/PR
- 📊 Relatórios de cobertura online
- 🚫 Não precisa instalar nada localmente

### Opção 2: Script Principal (Local)
Execute o script principal que roda todos os testes automaticamente:

```bash
# No diretório raiz do projeto
python run_all_tests.py
```

Este script:
- ✅ Instala todas as dependências automaticamente
- ✅ Executa migrações do banco
- ✅ Roda testes do backend e frontend
- ✅ Gera relatórios de cobertura
- ✅ Mostra resumo completo dos resultados

### Opção 2: Scripts Individuais
Se preferir executar separadamente:

#### Backend
```bash
cd testalready/backend
python run_tests.py
```

#### Frontend
```bash
cd testalready/frontend
python run_tests.py
```

## 🔧 Execução Manual (Para Desenvolvedores)

### Backend (Django)

#### 1. Navegar para o diretório
```bash
cd testalready/backend
```

#### 2. Instalar dependências
```bash
pipenv install --dev
```

#### 3. Ativar ambiente virtual
```bash
pipenv shell
```

#### 4. Executar migrações
```bash
python manage.py migrate
```

#### 5. Executar testes
```bash
# Testes básicos
pipenv run pytest -v

# Testes com cobertura
pipenv run pytest --cov=savedate --cov-report=html --cov-report=term-missing

# Testes específicos
pipenv run pytest savedate/tests/ -v
```

### Frontend (React)

#### 1. Navegar para o diretório
```bash
cd testalready/frontend
```

#### 2. Instalar dependências
```bash
npm install
```

#### 3. Executar testes
```bash
# Testes básicos
npm test

# Testes com cobertura
npm run test:cov

# Testes em modo watch
npm run test:ui
```

## 📊 Relatórios de Cobertura

### Backend
- **Localização**: `testalready/backend/htmlcov/index.html`
- **Formato**: HTML interativo
- **Comando**: `pipenv run pytest --cov=savedate --cov-report=html`

### Frontend
- **Localização**: `testalready/frontend/coverage/lcov-report/index.html`
- **Formato**: HTML interativo
- **Comando**: `npm run test:cov`

## 🧪 Estrutura dos Testes

### Backend
```
testalready/backend/savedate/
├── test_models.py      # Testes do modelo SaveDate
├── test_serializers.py # Testes dos serializers
└── test_views.py       # Testes das views/API endpoints
```

**Cobertura dos Testes:**
- ✅ **Modelos**: Validações, campos obrigatórios, formatos
- ✅ **Serializers**: Validação de entrada/saída, campos obrigatórios
- ✅ **Views**: Endpoints da API, cenários válidos e inválidos
- ✅ **Integração**: Fluxo completo de criação de eventos

### Frontend
```
testalready/frontend/src/test/
├── unit/               # Testes unitários
│   ├── InputField.test.tsx
│   ├── TimePickerField.test.tsx
│   └── smoke.test.tsx
├── integration/        # Testes de integração
│   ├── FormUsingInputField.test.tsx
│   └── EventTimesField.integration.test.tsx
└── __utils__/         # Utilitários de teste
```

**Cobertura dos Testes:**
- ✅ **Componentes**: InputField, TimePickerField, EventTimesField
- ✅ **Formulários**: Validação, interação do usuário, submissão
- ✅ **Integração**: Fluxo completo de formulários

## 🎯 Cenários de Teste

### Backend - API Endpoints
- ✅ Criação de evento com dados válidos
- ✅ Criação de evento sem campos opcionais
- ✅ Validação de campos obrigatórios
- ✅ Validação de formatos (título, descrição, endereço)
- ✅ Validação de horários (formato 24h)
- ✅ Tratamento de erros de validação
- ✅ Listagem de eventos
- ✅ Tratamento de JSON inválido

### Frontend - Componentes
- ✅ Renderização correta dos componentes
- ✅ Validação de formulários
- ✅ Interação do usuário
- ✅ Submissão de formulários
- ✅ Tratamento de erros
- ✅ Estados de loading e sucesso

## 🚨 Solução de Problemas

### Erro: "pipenv not found"
```bash
pip install pipenv
```

### Erro: "python not found"
- Windows: Use `python` ou `py`
- macOS/Linux: Use `python3`

### Erro: "npm not found"
```bash
# Instalar Node.js de: https://nodejs.org/
```

### Testes falhando no Backend
1. Verifique se as migrações foram executadas
2. Verifique se o ambiente virtual está ativo
3. Execute: `pipenv run python manage.py check`

### Testes falhando no Frontend
1. Verifique se as dependências foram instaladas
2. Execute: `npm install`
3. Verifique se o Node.js está atualizado

## 📝 Comandos Úteis

### Backend
```bash
# Verificar configuração do Django
pipenv run python manage.py check

# Criar migrações (se necessário)
pipenv run python manage.py makemigrations

# Aplicar migrações
pipenv run python manage.py migrate

# Shell do Django
pipenv run python manage.py shell
```

### Frontend
```bash
# Limpar cache
npm run build -- --force

# Verificar dependências
npm audit

# Atualizar dependências
npm update
```

## 🎉 Sucesso!

Quando todos os testes passarem, você verá:

```
🎉 TODOS os testes foram executados com sucesso!
✅ Backend: OK
✅ Frontend: OK

📁 Relatórios gerados:
   - Backend: testalready/backend/htmlcov/index.html
   - Frontend: testalready/frontend/coverage/lcov-report/index.html
```

## 🚀 GitHub Actions (CI/CD)

### Como Funciona
O projeto está configurado com GitHub Actions que executam automaticamente:

1. **Testes do Backend** (Django + pytest)
2. **Testes do Frontend** (React + Vitest)
3. **Script Principal** (validação completa)

### Configuração
- **Arquivo**: `.github/workflows/ci.yml`
- **Triggers**: Push para `main/master/develop` e Pull Requests
- **Ambiente**: Ubuntu Latest com Python 3.12 e Node.js 18

### Relatórios de Cobertura
- **Backend**: XML + terminal
- **Frontend**: LCOV + HTML
- **Integração**: Codecov (se configurado)

### Monitoramento
- Acesse a aba "Actions" no GitHub
- Veja o status de cada job
- Baixe logs detalhados
- Verifique relatórios de cobertura

### Vantagens do GitHub Actions
- ⚡ **Execução paralela** dos testes
- 🔄 **Automático** a cada push/PR
- 📊 **Relatórios online** de cobertura
- 🚫 **Não precisa instalar** nada localmente
- 📱 **Acesso de qualquer lugar** via GitHub

## 📞 Suporte

Se encontrar problemas:
1. Verifique os logs de erro acima
2. Execute os testes manualmente em cada diretório
3. Verifique se todas as dependências estão instaladas
4. Certifique-se de estar no diretório correto

---

**Boa sorte com os testes! 🚀**
