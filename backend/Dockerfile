FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta que o FastAPI vai rodar
EXPOSE 8000

# Comando para iniciar a aplicação (será sobrescrito pelo docker-compose)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
