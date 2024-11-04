# Projeto Visitantes - Backend V1

Este projeto visa melhorar e otimizar o processo de registro dos visitantes de uma igreja, oferecendo uma solução organizada e eficiente para armazenar e gerenciar os dados dos visitantes. Ele facilita a anotação e acompanhamento das informações, como nome, cidade, igreja de origem e data da visita, permitindo um controle detalhado das visitas recebidas.

## Funcionalidades

- **Registro de Visitantes**: Cadastro de visitantes com informações como nome, cidade, igreja de origem e data da visita.
- **Consulta de Visitas e Visitantes**: Listagem e busca de visitas e visitantes registrados, organizados por data.
- **Gerenciamento de Dados**: Edição, atualização e exclusão de registros conforme necessário.

## Tecnologias Utilizadas

- **Python** e **Flask** para o desenvolvimento da API RESTful.
- **SQLAlchemy** para manipulação do banco de dados.
- **Logging** para monitoramento de atividades e erros.

## Como Rodar o Projeto

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu_usuario/projeto-visitantes.git
   cd projeto-visitantes
   
2. **Crie um Ambiente Virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv```
   source venv/bin/activate  # Linux ou macOS
   venv\Scripts\activate     # Windows

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

4. **Inicialize o Banco de Dados:**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade

5. **Rodar a aplicação:**
   ```bash
   flask run
