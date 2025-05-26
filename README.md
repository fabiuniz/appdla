# 🚀 Desafio 21 Dias de Código Fonte TV: Reengenharia de Funções JavaScript para uma Aplicação Full-Stack

Este projeto representa uma reengenharia e modernização de uma série de exercícios de lógica e estruturas de dados originalmente em JavaScript. O objetivo foi transformar essas funcionalidades isoladas em uma aplicação web completa e interativa, utilizando uma arquitetura de backend (FastAPI em Python) e frontend (React com Tailwind CSS).

Como Analista de Sistemas, esta abordagem demonstra não apenas a capacidade de resolver problemas lógicos, mas também a proficiência em projetar e implementar soluções escaláveis, modulares e com foco na experiência do usuário.

## 🎯 Visão Geral do Projeto

O projeto consiste em:

* **Backend (API):** Desenvolvido com **FastAPI** em Python, expondo cada funcionalidade JavaScript como um endpoint RESTful. Isso permite que a lógica de negócio seja desacoplada da interface do usuário.
* **Frontend (Interface Web):** Construído com **React** e estilizado com **Tailwind CSS**, oferecendo uma interface intuitiva para interagir com cada função da API. A organização por "Dias" reflete a progressão dos desafios originais, facilitando a exploração.

## 💡 Abordagem e Conhecimento de Analista de Sistemas

Esta solução reflete princípios cruciais de um experiente Analista de Sistemas:

1.  **Modularidade e Separação de Responsabilidades:**
    * **Backend como Serviço:** Cada "função" é agora um serviço bem definido, acessível via API. Isso promove a reutilização de código e facilita a manutenção, pois alterações em uma funcionalidade não afetam diretamente outras partes do sistema.
    * **Frontend Desacoplado:** A interface do usuário é independente da lógica de negócio. Isso permite que o frontend seja desenvolvido e implantado separadamente, além de facilitar futuras migrações de tecnologia ou a criação de novas interfaces (ex: mobile).

2.  **Escalabilidade e Manutenibilidade:**
    * A arquitetura de API permite que o backend seja escalado horizontalmente (adicionando mais instâncias do FastAPI) independentemente do frontend.
    * A organização clara por "Dias" e a modularização das funções no backend facilitam a identificação, depuração e adição de novas funcionalidades.

3.  **Reusabilidade e Padronização:**
    * As funções JavaScript originais foram convertidas em endpoints de API padronizados, utilizando modelos **Pydantic** para validação de dados de entrada e saída. Isso garante a consistência e a segurança das interações.
    * Componentes React reutilizáveis foram criados para a interface, agilizando o desenvolvimento e mantendo a uniformidade visual.

4.  **Experiência do Desenvolvedor (DX):**
    * A escolha de **FastAPI** (performance, documentação automática via Swagger UI) e **React** (componentização, reatividade) oferece uma excelente experiência de desenvolvimento, acelerando o ciclo de vida do software.
    * O uso de **Tailwind CSS** agiliza a estilização e garante um design responsivo e moderno sem a necessidade de escrever CSS complexo.

5.  **Demonstração de Conhecimento Abrangente:**
    * **Lógica de Programação:** As funções convertidas cobrem uma vasta gama de conceitos, desde operações básicas e condicionais até loops, estruturas de dados (filas, pilhas, deques, listas encadeadas) e algoritmos de busca/ordenação.
    * **Desenvolvimento Web:** Conhecimento em APIs RESTful, comunicação cliente-servidor, gerenciamento de estado no frontend e construção de interfaces interativas.
    * **Engenharia de Software:** Aplicação de princípios de design de sistemas, modularidade e tratamento de erros.

## 🛠️ Tecnologias Utilizadas

* **Backend:**
    * **Python:** Linguagem de programação principal.
    * **FastAPI:** Framework web para construção de APIs de alta performance.
    * **Pydantic:** Para validação e serialização de dados.
    * **`collections.deque`:** Para a implementação do Deque.
    * **`numpy` / `pandas` / `tensorflow` / `scikit-learn` / `joblib`:** (Opcional, se o projeto de turnover estiver integrado e usar ML)

* **Frontend:**
    * **React:** Biblioteca JavaScript para construção de interfaces de usuário.
    * **Tailwind CSS:** Framework CSS utilitário para estilização rápida e responsiva.
    * **Babel:** Para transpilar JSX e JavaScript moderno.
    * **`fetch` API:** Para comunicação com o backend.

## 📦 Funcionalidades Demonstradas

O projeto demonstra a interatividade com as seguintes categorias de funcionalidades (organizadas por "Dias"):

* **Dia 03: Operações Básicas** (Soma, Subtração, Multiplicação, Cálculo de Idade, Média, Conversões).
* **Dia 04: Condicionais** (Renovação CNH, Avaliação de Notas, Ternário, Elegibilidade de Compra, Status de Cancela, Desconto de Produto).
* **Dia 05: Loops** (Juros Compostos, Contagem Regressiva, Tempo para Dobrar Investimento, Cálculo de Parcelas).
* **Dia 06: Funções** (Calculadora de IMC, Obter Dia da Semana, Cálculo de Investimento).
* **Dia 07: Sistema Bancário** (Depósito, Débito, Transferência, Conversão para Dólar, Status de Conta - **Estado em memória**).
* **Dia 08: Fila Simples** (Entrar/Sair da Fila, Status - **Estado em memória**).
* **Dia 09: Operações com Arrays/Listas** (IndexOf, Includes, LastIndexOf, Extrair Porção).
* **Dia 10 & 11: Pilha (Stack)** (Empilhamento de Produtos, Navegação de Browser - **Estado em memória**).
* **Dia 12: Fila Drive-Thru** (Entrar/Atender Carro, Status - **Estado em memória**).
* **Dia 13: Deque (Gerenciamento de Tarefas)** (Adicionar/Remover Início/Fim, Ajustar Prioridade - **Estado em memória**).
* **Dia 14: Múltiplas Filas (Caixas)** (Adicionar/Atender Clientes em Múltiplas Filas - **Estado em memória**).
* **Dia 15: Lista Encadeada** (Inserir/Remover em Posições, Buscar, Percorrer - **Estado em memória**).
* **Dia 16 & 18: Playlist** (Adicionar/Remover/Mover Música, Tocar, Ordenar por Nome/Reproduções - **Estado em memória**).
* **Dia 17: Ordenação de Arrays** (Ordenar Produtos por Nome/Preço).
* **Dia 19: Recursão (Cálculo de Fatura)** (Cálculo de total de faturas aninhadas).
* **Dia 20: Recursão (Busca)** (Busca Binária, Busca de Mensagens por Palavra).
* **Dia 21: Sistema Bancário Pix** (Enviar/Cancelar Pix, Status - **Estado em memória**).

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para configurar e rodar a aplicação em seu ambiente local:

1.  **Clone o Repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [nome_da_pasta_do_projeto]
    ```

2.  **Configurar o Backend (FastAPI):**
    * Crie um ambiente virtual (recomendado):
        ```bash
        python -m venv venv
        # No Windows:
        .\venv\Scripts\activate
        # No macOS/Linux:
        source venv/bin/activate
        ```
    * Instale as dependências:
        ```bash
        pip install -r requirements.txt
        ```
        (Certifique-se de que `requirements.txt` contém `fastapi`, `uvicorn`, `pydantic`, `collections-extended` (para deque se não for nativo), etc. conforme o `main.py` usa.)
    * Execute o servidor FastAPI:
        ```bash
        uvicorn main:app --reload
        ```
        O backend estará acessível em `http://127.0.0.1:8000`. Você pode testar os endpoints através da documentação interativa em `http://127.0.0.1:8000/docs`.

3.  **Configurar e Acessar o Frontend (React):**
    * O frontend é composto por `index.html` e `App.jsx`. Para executá-lo, você pode usar um servidor HTTP simples na mesma pasta.
    * Na pasta raiz do projeto, execute:
        ```bash
        python -m http.server 3000
        ```
    * Abra seu navegador e acesse `http://vmlinuxd:3000`.

## 📈 Melhorias Futuras

* **Persistência de Dados:** Integrar um banco de dados (ex: PostgreSQL, MongoDB, Firestore) para que o estado das estruturas de dados e do sistema bancário seja persistente e não se perca ao reiniciar o servidor.
* **Autenticação e Autorização:** Implementar um sistema de login para proteger certos endpoints.
* **Testes Automatizados:** Adicionar testes unitários e de integração para garantir a robustez das funcionalidades.
* **Containerização:** Empacotar a aplicação em contêineres Docker para facilitar o deploy e a portabilidade.
* **Interface do Usuário:** Aprimorar o design e a responsividade, talvez com bibliotecas de componentes UI mais avançadas.
* **Documentação da API:** Gerar documentação mais detalhada para cada endpoint e seus modelos.

Este projeto é uma prova prática da capacidade de transformar conceitos de programação em soluções de software funcionais e bem estruturadas, um diferencial para qualquer Analista de Sistemas.
