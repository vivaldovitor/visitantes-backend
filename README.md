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
   - Copie e cole no terminal para clonar o projeto
   ```
   git clone https://github.com/vivaldovitor/projeto-visitantes.git
   ```
   - Abra o projeto
   ```
   cd projeto-visitantes
   ```
   
2. **Crie um Ambiente Virtual (opcional, mas recomendado):**
   - Ubunto
   ```
   virtualenv venv
   ```
   - Linux
   ```
   source venv/bin/activate
   ```
   - Windows
   ```
   venv/Scripts/activate
   ```
3. **Instale as dependências:**
   - Para instalar as dependências e os arquivos que estão no arquivo requirements.txt, execute:
   ```
   pip install -r requirements.txt
   ```
4. **Inicialize o Banco de Dados:**
   - Inicializar migrações
   ```
   flask db init
   ```
   - Realiza uma nova migração de acordo com as mudanças feitas
   ```
   flask db migrate -m "Migração inicial"
   ```
   - Adiciona a migração ao banco de dados
   ```
   flask db upgrade
   ```

5. **Rodar a aplicação:**
   ```
   flask run
   ```
