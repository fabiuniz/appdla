# --- Stage 1: Build da aplicação React ---
# Usa uma imagem Node.js mais recente para o build
FROM node:20-alpine AS builder

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# --- CORREÇÃO AQUI: Copie os arquivos de configuração de dependência primeiro ---
# Isso garante que 'npm install' encontre o package.json
COPY package.json ./

# Instala as dependências do Node.js
# Isso aproveita o cache do Docker se as dependências não mudarem
RUN npm install

# Copia todo o restante do código da aplicação
# Certifique-se de que App.jsx, index.html, webpack.config.js, etc.,
# estão na raiz do diretório 'frontend' local que você está copiando.
COPY . .

# Se você realmente tem arquivos com a extensão .cs que deveriam ser .css,
# CORRIJA ISSO NO SEU CÓDIGO FONTE LOCALMENTE ANTES DO BUILD!
# Comentado, pois é melhor corrigir na origem.
# RUN mv ./static/main.cs ./static/main.css || true
# RUN mv ./styles.cs ./styles.css || true

# Executa o comando de build do Webpack definido no package.json
# Este comando deve gerar os arquivos otimizados na pasta 'dist' (ou 'build' etc.)
RUN npm run build

# --- Stage 2: Servir a aplicação construída com Nginx ---
# Usa uma imagem Nginx estável e leve
FROM nginx:stable-alpine

# Remove a configuração padrão do Nginx para usar a sua
RUN rm /etc/nginx/conf.d/default.conf

# Copia sua configuração Nginx personalizada
# Certifique-se de que o nginx.conf está no mesmo diretório do Dockerfile
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copia os arquivos da aplicação construída (do stage 'builder') para o diretório de serviço do Nginx
# Certifique-se de que '/app/dist' é o caminho de saída configurado no seu webpack.config.js
COPY --from=builder /app/dist /usr/share/nginx/html

# Expõe a porta que o Nginx vai escutar dentro do contêiner.
# Se seu nginx.conf dentro do contêiner escuta na porta 80, mude para EXPOSE 80.
# Se ele escuta na 3000, mantenha EXPOSE 3000.
# A porta externa (do host) é definida no docker-compose.yml.
EXPOSE 3000

# Comando padrão para iniciar o Nginx em foreground
CMD ["nginx", "-g", "daemon off;"]