#!/usr/bin/env python
"""
Script para executar testes do frontend de forma fácil.
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
    print("🚀 Iniciando execução dos testes do frontend...")
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("package.json"):
        print("❌ Erro: Este script deve ser executado no diretório frontend/")
        print("   Navegue para o diretório frontend/ e execute novamente.")
        sys.exit(1)
    
    # 1. Instalar dependências
    print("\n📦 Instalando dependências...")
    if not run_command("npm install", "Instalando dependências npm"):
        print("❌ Falha ao instalar dependências.")
        sys.exit(1)
    
    # 2. Executar testes
    print("\n🧪 Executando testes...")
    if not run_command("npm test", "Executando testes"):
        print("❌ Alguns testes falharam. Verifique os erros acima.")
        sys.exit(1)
    
    # 3. Executar testes com cobertura
    print("\n📊 Executando testes com cobertura...")
    if not run_command("npm run test:cov", "Executando testes com cobertura"):
        print("❌ Falha ao executar testes com cobertura.")
        sys.exit(1)
    
    print("\n🎉 Todos os testes foram executados com sucesso!")
    print("📁 Relatório de cobertura gerado em: coverage/")
    print("🔍 Para ver o relatório, abra coverage/lcov-report/index.html no seu navegador.")

if __name__ == "__main__":
    main()
