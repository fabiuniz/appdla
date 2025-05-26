#setup.sh
pip install -r requirements.txt

uvicorn main:app --reload
http://127.0.0.1:8000
# Na pasta 'your_project/'
python -m http.server 3000

docker-compose up --build
docker-compose up --build --no-cache


# cp *.deb /var/cache/apt/archives; rm *.deb
# docker load -i python_3.9-slim.tar; rm python_3.9-slim.tar
# . setup_script_launcher.sh
# docker load -i python_3.9-slim.tar
# mkdir -p /home/userlnx/docker/script_docker/appdla
# chmod -R 777 /home/userlnx/docker/script_docker/appdla
# up files appdla
# up files pacotespip
# up file python_3.9-slim.tar
# docker-compose up --build
# docker system prune -a --volumes; clear ; docker images;
# docker exec -it appdla_app_1 /bin/bash
# root@6d278194616b:/app/static# mv dados_funcionarios.csv dados_funcionarios_.csv
# docker cp dashboard.py appdla_app_1:/app/dashboard.py 
# docker logs -f appdla_app_1
# docker-compose down
# docker-compose up -d
# ufw allow 3000/tcp
# ufw allow 8000/tcp
# ufw reload


# which pip
# http://vmlinuxd:8000/predict/
# curl -X POST "http://vmlinuxd:8000/predict/" -H "Content-Type: application/json" -d '{"idade": 35, "salario": 8500, "tempo_empresa": 5, "avaliacao": 4.2}'
# pip download tensorflow -d /home/userlnx/docker/script_docker/relay/
# Backup: pip download -r <(pip freeze) -d /home/userlnx/docker/script_docker/relay
# Backup: pip download dash -d /home/userlnx/docker/script_docker/relay/
# Backup: pip download -r requirements.txt -d /home/userlnx/docker/script_docker/relay/
# restauração: pip install --no-index --find-links=/home/userlnx/docker/script_docker/relay -r requirements.txt
# curl -X POST -H "Content-Type: application/json" -d '{"input": "some_data"}' http://127.0.0.1:8051/api/process_data
# curl http://127.0.0.1:8050/
# ps aux | grep "python.*dashboard.py"
# tail -f your_app.log  # See the latest log entries in real-time grep "ERROR" your_app.log # Find lines containing "ERROR"
# pip download -r requirements.txt -d /home/userlnx/docker/script_docker/relay/
# 
# 
# 
# pip freeze > requirements.txt
# pip download --find-links=/bin/pip -r <(pip freeze) -d /home/userlnx/docker/script_docker/relay/
# 
# pip download dash -d /home/userlnx/docker/script_docker/relay/
# pip download fastapi -d /home/userlnx/docker/script_docker/relay/
# pip download matplotlib -d /home/userlnx/docker/script_docker/relay/
# pip download numpy -d /home/userlnx/docker/script_docker/relay/
# pip download pandas -d /home/userlnx/docker/script_docker/relay/
# pip download plotly -d /home/userlnx/docker/script_docker/relay/
# pip download pydantic -d /home/userlnx/docker/script_docker/relay/
# pip download requests -d /home/userlnx/docker/script_docker/relay/
# pip download scikit -d /home/userlnx/docker/script_docker/relay/
# pip download seaborn -d /home/userlnx/docker/script_docker/relay/
# pip download streamlit -d /home/userlnx/docker/script_docker/relay/
# pip download tensorflow -d /home/userlnx/docker/script_docker/relay/
# pip download uvicorn -d /home/userlnx/docker/script_docker/relay/
# 
# Restaurar pip install --no-index --find-links=/home/userlnx/docker/script_docker/relay/ -r requirements.txt

# pip show dash | awk '/^Version:/ { printf "dash==%s\n", $2 }'
# pip show fastapi | awk '/^Version:/ { printf "fastapi==%s\n", $2 }'
# pip show matplotlib | awk '/^Version:/ { printf "matplotlib==%s\n", $2 }'
# pip show numpy | awk '/^Version:/ { printf "numpy==%s\n", $2 }'
# pip show pandas | awk '/^Version:/ { printf "pandas==%s\n", $2 }'
# pip show plotly | awk '/^Version:/ { printf "plotly==%s\n", $2 }'
# pip show pydantic | awk '/^Version:/ { printf "pydantic==%s\n", $2 }'
# pip show requests | awk '/^Version:/ { printf "requests==%s\n", $2 }'
# pip show scikit-learn | awk '/^Version:/ { printf "scikit-learn==%s\n", $2 }'
# pip show seaborn | awk '/^Version:/ { printf "seaborn==%s\n", $2 }'
# pip show streamlit | awk '/^Version:/ { printf "streamlit==%s\n", $2 }'
# pip show tensorflow | awk '/^Version:/ { printf "tensorflow==%s\n", $2 }'
# pip show uvicorn | awk '/^Version:/ { printf "uvicorn==%s\n", $2 }'
# 
#!/bin/bash

# --- Step 1: Install Node.js and npm on the host system ---
echo "--- Checking for Node.js and npm on host... ---"

# Check if npm is installed
if ! command -v npm &> /dev/null
then
    echo "npm not found. Installing Node.js and npm..."
    # Update package list and install curl if needed
    sudo apt update
    sudo apt install -y curl

    # Download and execute the NodeSource setup script for Node.js 20
    # Use option B (download then execute) for robustness
    echo "Downloading NodeSource setup script..."
    curl -fsSL -o nodesource_setup.sh https://deb.nodesource.com/setup_20.x
    echo "Executing NodeSource setup script..."
    sudo bash nodesource_setup.sh
    rm nodesource_setup.sh # Clean up the downloaded script

    # Install Node.js (which includes npm)
    echo "Installing nodejs package..."
    sudo apt install -y nodejs
    echo "Node.js and npm installed successfully!"
else
    echo "Node.js and npm are already installed."
fi

# --- Step 2: Generate package-lock.json in frontend directory ---
echo "--- Navigating to frontend directory and running npm install... ---"
# Ensure we are in the script's directory, then move to frontend
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR/frontend"

# Check if package-lock.json exists, if not, run npm install
if [ ! -f "package-lock.json" ]; then
    echo "package-lock.json not found. Running npm install to generate it..."
    npm install
    if [ $? -eq 0 ]; then
        echo "npm install completed successfully and package-lock.json created."
    else
        echo "Error: npm install failed. Please check the output above."
        exit 1
    fi
else
    echo "package-lock.json already exists. Skipping npm install for lock file generation."
fi

# --- Step 3: Return to main appdla directory and run Docker Compose ---
echo "--- Returning to main directory and starting Docker Compose... ---"
cd "$SCRIPT_DIR"

# Clean up old images and re-build everything
echo "Stopping and removing old Docker containers/images..."
docker-compose down --rmi all

echo "Building and starting new Docker containers..."
docker-compose up --build

echo "--- Setup and Docker Compose run complete! ---"