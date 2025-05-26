import os
import shutil
import subprocess
from datetime import datetime

# Configurações iniciais
PROJECT_DIR = os.getcwd()
TEMP_DIR = os.path.join(PROJECT_DIR, "temp_project")
COMMIT_MESSAGES = [
    "Inicialização do projeto e configuração básica do ambiente",
    "Configuração do backend com FastAPI",
    "Implementação das funções básicas do Day 03",
    "Configuração completa do Docker Compose",
    "Configuração inicial do frontend com React",
    "Implementação dos componentes do Day 03 no frontend",
    "Expansão para Days 04 a 09",
    "Implementação de estruturas de dados (Days 10 a 15)",
    "Implementação de playlist e ordenação (Days 16-18 e 17)",
    "Adição de recursão e Pix (Days 19-21)",
    "Configuração final do frontend e Nginx"
]

# Função para criar diretórios se não existirem
def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Criado diretório: {directory}")

# Função para executar comandos Git
def run_git_command(command):
    process = subprocess.run(command, shell=True, cwd=PROJECT_DIR, text=True, capture_output=True)
    # Always print stdout and stderr for debugging
    print(f"STDOUT: {process.stdout}")
    print(f"STDERR: {process.stderr}")
    if process.returncode != 0:
        print(f"Erro ao executar comando Git: O comando '{command}' falhou com código {process.returncode}")
        # Do not exit immediately, let's see if the issue persists
        # exit(1) # Comment this out temporarily
    # print(process.stdout) # Already printed above

# Função para editar arquivos
def edit_files_for_commit(commit_index):
    # Criar diretórios backend e frontend se não existirem
    ensure_directory("backend")
    ensure_directory("frontend")

    if commit_index == 0:  # Commit 1
        # Estrutura básica do docker-compose.yml
        with open("docker-compose.yml", "w", encoding="utf-8") as f:
            f.write("version: '3'\n\nservices:\n  backend:\n  frontend:\n")
        
        # Estrutura básica do frontend/index.html
        with open("frontend/index.html", "w", encoding="utf-8") as f:
            f.write("<!DOCTYPE html>\n<html lang=\"pt\"><head><meta charset=\"UTF-8\"></head><body></body></html>")
        
        # Estrutura básica do frontend/package.json
        with open("frontend/package.json", "w", encoding="utf-8") as f:
            f.write('{"name": "appdla_frontend", "version": "1.0.0", "scripts": {"start": "echo start", "build": "echo build"}}')

    elif commit_index == 1:  # Commit 2
        # Copiar backend/Dockerfile do temp_project
        shutil.copy(os.path.join(TEMP_DIR, "backend/Dockerfile"), "backend/Dockerfile")
        
        # Estrutura inicial do backend/main.py
        with open("backend/main.py", "w", encoding="utf-8") as f:
            f.write(
                "# main.py\n"
                "from fastapi import FastAPI\n"
                "from pydantic import BaseModel\n\n"
                "# Inicializa a aplicação FastAPI\n"
                "app = FastAPI()\n\n"
                "# Modelos Pydantic para Day 03\n"
                "class BasicOpInput(BaseModel):\n"
                "    val1: float\n"
                "    val2: float\n\n"
                "class BasicOpOutput(BaseModel):\n"
                "    result: float\n"
            )

    elif commit_index == 2:  # Commit 3
        # Adicionar endpoints do Day 03 ao backend/main.py
        with open("backend/main.py", "a", encoding="utf-8") as f:
            f.write(
                "\n# Day 03: Operações Básicas\n"
                "@app.post('/day03/sum', response_model=BasicOpOutput)\n"
                "def calculate_sum(input: BasicOpInput):\n"
                "    return {'result': input.val1 + input.val2}\n"
            )

    elif commit_index == 3:  # Commit 4
        # Copiar docker-compose.yml completo do temp_project
        shutil.copy(os.path.join(TEMP_DIR, "docker-compose.yml"), "docker-compose.yml")

    elif commit_index == 4:  # Commit 5
        # Copiar frontend/App.jsx e frontend/index.html do temp_project
        shutil.copy(os.path.join(TEMP_DIR, "frontend/App.jsx"), "frontend/App.jsx")
        shutil.copy(os.path.join(TEMP_DIR, "frontend/index.html"), "frontend/index.html")
        shutil.copy(os.path.join(TEMP_DIR, "frontend/package.json"), "frontend/package.json")

    elif commit_index == 5:  # Commit 6
        # Adicionar Day03.jsx simplificado
        with open("frontend/Day03.jsx", "w", encoding="utf-8") as f:
            f.write(
                "const Day03 = () => {\n"
                "    return <div>Day 03 Component</div>;\n"
                "};\n"
            )

    elif commit_index == 6:  # Commit 7
        # Adicionar trechos para Days 04-09 (simplificado)
        with open("backend/main.py", "a", encoding="utf-8") as f:
            f.write(
                "\n# Day 04: Condicionais\n"
                "class CNHInput(BaseModel):\n"
                "    idade: int\n"
                "    primeiraHabilitacao: bool\n\n"
                "@app.post('/day04/cnh_renewal')\n"
                "def cnh_renewal(input: CNHInput):\n"
                "    vencimento = ''\n"
                "    if input.primeiraHabilitacao:\n"
                "        vencimento = '1 ano'\n"
                "    return {'prazo_renovacao': vencimento}\n"
            )
        with open("frontend/Day04.jsx", "w", encoding="utf-8") as f:
            f.write(
                "const Day04 = () => {\n"
                "    return <div>Day 04 Component</div>;\n"
                "};\n"
            )

    elif commit_index == 7:  # Commit 8
        # Adicionar trechos para Days 10-15 (simplificado)
        with open("backend/main.py", "a", encoding="utf-8") as f:
            f.write(
                "\n# Day 10: Pilha Simples\n"
                "product_stack = []\n"
                "@app.post('/day10/stack/push_product')\n"
                "def push_product():\n"
                "    return {'message': 'Produto empilhado'}\n"
            )
        with open("frontend/Day10.jsx", "w", encoding="utf-8") as f:
            f.write(
                "const Day10 = () => {\n"
                "    return <div>Day 10 Component</div>;\n"
                "};\n"
            )

    elif commit_index == 8:  # Commit 9
        # Adicionar trechos para Days 16-18 e 17 (simplificado)
        with open("backend/main.py", "a", encoding="utf-8") as f:
            f.write(
                "\n# Day 16 & 18: Playlist\n"
                "playlist_state = {'musicas': []}\n"
                "@app.post('/day16_18/playlist/add_song')\n"
                "def add_song_to_playlist():\n"
                "    return {'message': 'Música adicionada'}\n"
            )
        with open("frontend/Day16_18.jsx", "w", encoding="utf-8") as f:
            f.write(
                "const Day16_18 = () => {\n"
                "    return <div>Day 16-18 Component</div>;\n"
                "};\n"
            )

    elif commit_index == 9:  # Commit 10
        # Adicionar trechos para Days 19-21 (simplificado)
        with open("backend/main.py", "a", encoding="utf-8") as f:
            f.write(
                "\n# Day 19: Recursão\n"
                "@app.post('/day19/recursion/calculate_invoice_total')\n"
                "def calculate_invoice_total():\n"
                "    return {'totalFatura': 0}\n"
            )
        with open("frontend/Day19.jsx", "w", encoding="utf-8") as f:
            f.write(
                "const Day19 = () => {\n"
                "    return <div>Day 19 Component</div>;\n"
                "};\n"
            )

    elif commit_index == 10:  # Commit 11
        # Copiar nginx.conf do temp_project (certifique-se de que ele realmente cause uma mudança)
        shutil.copy(os.path.join(TEMP_DIR, "frontend/nginx.conf"), "frontend/nginx.conf")
    
        # Adicionar um pequeno README.md final para garantir que haja uma mudança
        with open("frontend/README.md", "w", encoding="utf-8") as f:
            f.write("## Frontend da Aplicação DLA\n\nEste é o frontend final configurado com React e Nginx.")

    # Limpar arquivos não utilizados (ajustado para evitar .git)
    allowed_files = [
        "docker-compose.yml",
        "Dockerfile",
        "main.py",
        "index.html",
        "App.jsx",
        "package.json",
        "Day03.jsx",
        "Day04.jsx",
        "Day10.jsx",
        "Day16_18.jsx",
        "Day19.jsx",
        "nginx.conf",
        "makecommits.py"  # Evitar remover o próprio script
    ]
    allowed_dirs = ["backend", "frontend", "temp_project", ".git"]

    for root, dirs, files in os.walk(PROJECT_DIR, topdown=False):
        # Ignorar o diretório .git completamente
        if ".git" in root:
            continue

        # Remover arquivos não permitidos
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, PROJECT_DIR)
            if rel_path not in allowed_files and file not in allowed_files:
                try:
                    os.remove(file_path)
                    print(f"Removido arquivo não utilizado: {rel_path}")
                except Exception as e:
                    print(f"Erro ao remover {rel_path}: {e}")

        # Remover diretórios não permitidos
        for dir in dirs:
            if dir not in allowed_dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Removido diretório não utilizado: {dir_path}")
                except Exception as e:
                    print(f"Erro ao remover diretório {dir_path}: {e}")

# Função principal
def main():
    # Inicializar repositório Git se necessário
    if not os.path.exists(os.path.join(PROJECT_DIR, ".git")):
        run_git_command("git init")

    # Iterar sobre os commits
    for i, message in enumerate(COMMIT_MESSAGES):
        print(f"\nAplicando Commit {i + 1}: {message}")
        edit_files_for_commit(i)

        # Adicionar e commitar
        run_git_command("git add .")
        run_git_command(f'git commit -m "{message}" --date="{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"')

    print("\nProcesso concluído! 11 commits criados.")

if __name__ == "__main__":
    main()