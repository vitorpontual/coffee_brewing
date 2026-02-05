Markdown

# ☕ Coffee Helper - Web Calculator

Uma calculadora web simples e elegante para entusiastas de café especial. O objetivo é calcular a quantidade ideal de água com base na gramatura dos grãos, respeitando o *ratio* (proporção) de cada método de extração.

## 🚀 Tecnologias
* **Python 3.13**
* **Flask** (Micro-framework web)
* **UV** (Gerenciador de pacotes e ambientes ultrarrápido)
* **Jinja2** (Templates HTML dinâmicos)
* **CSS3** (Interface responsiva)

## 📁 Estrutura do Projeto
```text
cafe/
├── config/
│   └── methods.py      # Configurações dos métodos de café (Português)
├── static/
│   └── style.css       # Estilização da interface
├── templates/
│   └── index.html      # Interface HTML
├── main.py             # Servidor Flask (Lógica em Inglês)
└── pyproject.toml      # Gerenciamento de dependências (uv)

🛠️ Como Rodar Localmente

    Instale o uv (caso não tenha):
    Bash

    curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh

    Crie o ambiente virtual e instale as dependências:
    Bash

    uv venv
    uv pip install flask gunicorn

    Execute a aplicação:
    Bash

    uv run main.py

    Acesse em: http://127.0.0.1:5000

📱 Acesso Mobile

Para acessar do celular na mesma rede Wi-Fi, descubra o IP do seu computador e rode o Flask permitindo conexões externas:
Bash

uv run flask --app main run --host=0.0.0.0

🌐 Deploy

Este projeto está pronto para ser hospedado no Render ou PythonAnywhere.

    Comando de Build: uv pip install -r requirements.txt

    Comando de Start: gunicorn main:app
