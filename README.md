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
   python -m venv venv

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

4. **Inicialize o Banco de Dados:**
   - Inicializar migrações
   ```bash
   flask db init
   flask db migrate -m "Migração inicial"
   flask db upgrade

5. **Rodar a aplicação:**
   ```bash
   flask run



**Dicas:**
- Ao formatar como um bloco de código, use três crases para iniciar e terminar o bloco, e escreva `bash` logo após as primeiras três crases para indicar que é código de terminal.
- Isso não só melhora a legibilidade, mas também permite que os usuários copiem facilmente os comandos para o terminal.

Se você precisar de mais assistência, é só avisar!
