# Testing Task Instructions

This project consists of a backend built with Django and a frontend built with React (using Vite and TypeScript).

As part of the task, we would like you to implement tests to demonstrate your skills and attention to quality.

## What we expect

### Frontend Testing

- Write **unit tests** for the `InputField` component to ensure it works correctly in isolation.
- Write **integration tests** for the overall form component that uses the `InputField`, validating user interaction and form submission behavior.
- Feel free to use testing tools like **Jest**, **React Testing Library**, or any other libraries you are comfortable with.

### Backend Testing

- Write tests for the API endpoint that creates an event, covering scenarios with valid and invalid inputs.
- You can use **pytest**, Django’s test framework, or any other Python testing tool you prefer.

Testing is a critical part of software development, and this task is designed to assess your ability to write maintainable, reliable tests.

## Submission Guidelines

- Please include the tests along with clear instructions on how to run them.
- The **deadline** for submitting this task is **Sunday at 6:00 PM**.

## 🧪 Executando os Testes

### 🚀 GitHub Actions (Mais Rápido - Automatizado)
Se o projeto estiver no GitHub, os testes são executados automaticamente:
- ✅ Push para qualquer branch ou Pull Request
- ✅ Acesse a aba "Actions" para ver resultados
- ✅ Relatórios de cobertura online
- ✅ Não precisa instalar nada localmente
- ✅ Workflow configurado: `.github/workflows/ci.yml`

### ⚡ Execução Rápida Local
Para executar todos os testes de uma vez:

```bash
# No diretório raiz do projeto
python run_all_tests.py
```

### 📚 Guia Detalhado
Consulte o arquivo `TESTING_README.md` para instruções completas sobre:
- Como executar testes individuais
- Solução de problemas
- Relatórios de cobertura
- Estrutura dos testes
- Configuração do GitHub Actions

### 🎯 O que foi implementado
- ✅ **Backend**: Testes completos para modelos, serializers e API endpoints
- ✅ **Frontend**: Testes unitários e de integração para componentes
- ✅ **Scripts**: Automação completa da execução de testes
- ✅ **Documentação**: Guias detalhados para facilitar a execução
- ✅ **GitHub Actions**: CI/CD automatizado com execução paralela
- ✅ **Codecov**: Relatórios de cobertura online (opcional)

---

If you have any questions or need clarification, feel free to reach out.


## Getting Started

### 1. Clone the repository

Clone this repository to your local machine using the following command:

```bash
https://github.com/edijavier99/test_full_stack

### 1. Navigate to the project directory

```bash
cd backend/
```

### 2. Install dependencies and activate the virtual environment (BACKEND)

Install pipenv (if not installed)

```bash
pip install pipenv

```

Then, run 

```bash
pipenv install
pipenv shell
```

### 3. Apply migrations

**On macOS/Linux:**

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

**On Windows:**

```bash
python manage.py makemigrations
python manage.py migrate
```


FRONTEND(VITE + REACT + TS)

### 1. Navigate to frontend folder

```bash
cd frontend 
```


### 2. Install npm dependencies

```bash
 npm install  
```

### 2. Run code 

```bash
 npm run dev
```




