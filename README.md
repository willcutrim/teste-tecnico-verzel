# Projeto Locação Dev

## Requisitos

- Python 3.8
- Docker
- Git

## Passos para executar o projeto

1. Clone o repositório:

    ```bash
    git clone <URL_DO_REPOSITORIO>
    ```

2. Entre na pasta do projeto:

    ```bash
    cd projeto_locacao_dev
    ```

3. Crie um ambiente virtual:

    ```bash
    python3.8 -m venv venv
    ```

4. Ative o ambiente virtual:

    - No Linux/MacOS:
        ```bash
        source venv/bin/activate
        ```
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```

5. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

6. Execute o Docker:

    - Para Docker Compose V1:
        ```bash
        docker-compose up -d
        ```
    - Para Docker Compose V2:
        ```bash
        docker compose up --build -d
        ```

7. Execute as migrações do Django:

    ```bash
    python manage.py migrate
    ```

8. Inicie o servidor Django:

    ```bash
    python manage.py runserver
    ```

Agora você pode acessar o projeto em `http://127.0.0.1:8000`.