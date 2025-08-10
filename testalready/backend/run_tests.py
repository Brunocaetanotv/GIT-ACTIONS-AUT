#!/usr/bin/env python
"""
Script para executar testes do backend de forma fácil.
Este script instala as dependências necessárias e executa os testes.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Executa um comando e mostra o resultado."""
    print(f"\n{'='*60}")
    print(f"🔄 {description}")
    print(f"{'='*60}")
    print(f"Executando: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ Sucesso!")
        if result.stdout:
            print("Saída:")
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Erro!")
        print(f"Código de saída: {e.returncode}")
        if e.stdout:
            print("Saída padrão:")
            print(e.stdout)
        if e.stderr:
            print("Erro:")
            print(e.stderr)
        return False

def main():
    """Função principal."""
    print("🚀 Iniciando execução dos testes do backend...")
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("manage.py"):
        print("❌ Erro: Este script deve ser executado no diretório backend/")
        print("   Navegue para o diretório backend/ e execute novamente.")
        sys.exit(1)
    
    # 1. Instalar dependências de teste
    print("\n📦 Instalando dependências de teste...")
    if not run_command("pipenv install --dev", "Instalando dependências de desenvolvimento"):
        print("❌ Falha ao instalar dependências. Verifique se o pipenv está instalado.")
        sys.exit(1)
    
    # 2. Ativar ambiente virtual
    print("\n🐍 Ativando ambiente virtual...")
    if not run_command("pipenv shell --exec python -c 'print(\"Ambiente ativado\")'", "Verificando ambiente virtual"):
        print("❌ Falha ao ativar ambiente virtual.")
        sys.exit(1)
    
    # 3. Executar migrações
    print("\n🗄️ Executando migrações...")
    if not run_command("pipenv run python manage.py migrate", "Executando migrações"):
        print("❌ Falha ao executar migrações.")
        sys.exit(1)
    
    # 4. Executar testes com pytest
    print("\n🧪 Executando testes...")
    if not run_command("pipenv run pytest -v --tb=short", "Executando testes com pytest"):
        print("❌ Alguns testes falharam. Verifique os erros acima.")
        sys.exit(1)
    
    # 5. Executar testes com cobertura
    print("\n📊 Executando testes com cobertura...")
    if not run_command("pipenv run pytest --cov=savedate --cov-report=html --cov-report=term-missing", "Executando testes com cobertura"):
        print("❌ Falha ao executar testes com cobertura.")
        sys.exit(1)
    
    print("\n🎉 Todos os testes foram executados com sucesso!")
    print("📁 Relatório de cobertura gerado em: htmlcov/index.html")
    print("🔍 Para ver o relatório, abra htmlcov/index.html no seu navegador.")

if __name__ == "__main__":
    main()
