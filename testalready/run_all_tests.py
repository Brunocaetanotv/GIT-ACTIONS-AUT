#!/usr/bin/env python
"""
Script principal para executar todos os testes do projeto.
Este script executa os testes do backend e frontend em sequência.
"""

import subprocess
import sys
import os

def run_command(command, description, cwd=None):
    """Executa um comando e mostra o resultado."""
    print(f"\n{'='*80}")
    print(f"🔄 {description}")
    print(f"{'='*80}")
    print(f"Executando: {command}")
    if cwd:
        print(f"Diretório: {cwd}")
    
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            capture_output=True, 
            text=True,
            cwd=cwd
        )
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
    print("🚀 Iniciando execução de TODOS os testes do projeto...")
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("testalready"):
        print("❌ Erro: Este script deve ser executado no diretório raiz do projeto")
        print("   Certifique-se de estar no diretório que contém a pasta 'testalready'")
        sys.exit(1)
    
    backend_dir = os.path.join("testalready", "backend")
    frontend_dir = os.path.join("testalready", "frontend")
    
    # Verificar se os diretórios existem
    if not os.path.exists(backend_dir):
        print(f"❌ Erro: Diretório backend não encontrado em {backend_dir}")
        sys.exit(1)
    
    if not os.path.exists(frontend_dir):
        print(f"❌ Erro: Diretório frontend não encontrado em {frontend_dir}")
        sys.exit(1)
    
    print(f"📁 Backend: {backend_dir}")
    print(f"📁 Frontend: {frontend_dir}")
    
    # 1. Executar testes do backend
    print("\n🐍 Executando testes do BACKEND...")
    if not run_command("python run_tests.py", "Executando script de testes do backend", cwd=backend_dir):
        print("❌ Falha ao executar testes do backend.")
        print("   Verifique os erros acima e tente executar manualmente.")
        backend_success = False
    else:
        backend_success = True
        print("✅ Testes do backend executados com sucesso!")
    
    # 2. Executar testes do frontend
    print("\n⚛️ Executando testes do FRONTEND...")
    if not run_command("python run_tests.py", "Executando script de testes do frontend", cwd=frontend_dir):
        print("❌ Falha ao executar testes do frontend.")
        print("   Verifique os erros acima e tente executar manualmente.")
        frontend_success = False
    else:
        frontend_success = True
        print("✅ Testes do frontend executados com sucesso!")
    
    # 3. Resumo final
    print(f"\n{'='*80}")
    print("📊 RESUMO DOS TESTES")
    print(f"{'='*80}")
    
    if backend_success and frontend_success:
        print("🎉 TODOS os testes foram executados com sucesso!")
        print("✅ Backend: OK")
        print("✅ Frontend: OK")
        print("\n📁 Relatórios gerados:")
        print("   - Backend: testalready/backend/htmlcov/index.html")
        print("   - Frontend: testalready/frontend/coverage/lcov-report/index.html")
    elif backend_success:
        print("⚠️  Testes executados com resultados mistos:")
        print("✅ Backend: OK")
        print("❌ Frontend: FALHOU")
    elif frontend_success:
        print("⚠️  Testes executados com resultados mistos:")
        print("❌ Backend: FALHOU")
        print("✅ Frontend: OK")
    else:
        print("❌ TODOS os testes falharam!")
        print("❌ Backend: FALHOU")
        print("❌ Frontend: FALHOU")
        print("\n🔧 Dicas para resolver:")
        print("   1. Verifique se todas as dependências estão instaladas")
        print("   2. Execute os testes manualmente em cada diretório")
        print("   3. Verifique os logs de erro acima")
        sys.exit(1)

if __name__ == "__main__":
    main()
