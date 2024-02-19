# D2W Lista de Tarefas

A **D2W Lista de Tarefas** é uma aplicação web interativa projetada para facilitar a gestão de tarefas pendentes pelos usuários. Utilizando uma interface intuitiva, os usuários podem facilmente criar, visualizar, modificar e excluir tarefas. Este projeto é desenvolvido com **React** no front-end e **Flask** no back-end, proporcionando uma experiência de usuário ágil e responsiva.

## Tecnologias Utilizadas

### Front-end
- **React**: Biblioteca JavaScript para construção de interfaces de usuário.
- **Redux e Redux Toolkit**: Ferramentas para gerenciamento de estado em aplicações JavaScript.
- **Ant Design**: Biblioteca de design para enriquecer a interface do usuário.
- **Axios**: Cliente HTTP baseado em promessas para fazer requisições.

### Back-end
- **Flask**: Microframework para Python com foco em simplicidade e flexibilidade.
- **Flask-CORS**: Extensão para Flask que lida com o compartilhamento de recursos entre origens (CORS).
- **Flask-JWT-Extended**: Extensão para Flask que facilita a utilização de JSON Web Tokens.
- **Flask-SQLAlchemy**: Extensão para Flask que adiciona suporte ao SQLAlchemy (ORM).

## Documentação [![Documentação](https://run.pstmn.io/button.svg)](https://www.postman.com/technical-pilot-11966957/workspace/d2w-to-do-list-colleciton/collection/21412589-6cedcc2d-f2bc-46fe-bf7e-136796802c32?action=share&creator=21412589)






A documentação da API está disponível através de uma collection no Postman, facilitando o teste e a integração das funcionalidades da aplicação.

## Executando a Aplicação

Para executar a **D2W Lista de Tarefas** localmente, siga os passos abaixo:

1. Clone o repositório:

```Bash
git clone https://github.com/GabrielPesch/d2w-to-do-list.git
````

2. Acesse o diretório do projeto:

```bash
cd d2w-to-do-list
```

3. Inicie o Docker Compose para subir a aplicação:

```bash
docker compose up
```
Acessando a Aplicação
Acesse a Aplicação via Navegador:

Com os serviços rodando, abra seu navegador e clique no link abaixo para acessar a interface da D2W Lista de Tarefas:

http://localhost:3000

Cadastro e Login:

Você pode cadastrar um novo usuário ou utilizar um usuário de testes. Para fins de exemplo, as credenciais do usuário de teste são:

senha:
Usuário: usertest@example.com
Senha:  minhasenhaSegur@1!


## Funcionalidades

- **Cadastro de Usuários**: Permite a criação de contas de usuários para acesso personalizado.
- **Listagem de Tarefas**: Exibe todas as tarefas cadastradas pelo usuário.
- **Filtragem de Tarefas**: Oferece a opção de filtrar tarefas por critérios específicos.
- **Conclusão de Tarefas**: Permite marcar tarefas como concluídas.
- **Exclusão de Tarefas**: Habilita a remoção de tarefas indesejadas da lista.

## Possíveis Erros da API

Durante a interação com a API, os seguintes erros podem ser encontrados, com suas mensagens traduzidas para o português:

- `missing_field_error`: "O campo {field} deve ser fornecido."
- `invalid_email_error`: "{email} não é um endereço de e-mail válido."
- `invalid_type_error`: "O campo {field} deve ser do tipo {field_type}."
- `field_min_size_error`: "O campo {field} deve ter no mínimo {min_size} caracteres."
- `field_max_size_error`: "O campo {field} não deve exceder {max_size} caracteres."
- `email_already_registered_error`: "O e-mail: [{email}] já está registrado."
- `invalid_credentials_error`: "Credenciais inválidas fornecidas."
- `user_not_found_error`: "Usuário não encontrado com {field} igual a {value}."
- `field_must_be_positive_error`: "O campo {field} deve ser um número inteiro positivo."
- `field_must_be_lower_than_error`: "O campo {field} deve ser menor que {value}."
- `entity_not_found_error`: "A entidade não pôde ser encontrada."
- `unauthorized_error`: "Você não está autorizado."

## Mensagens de Sucesso

Quando operações são concluídas com sucesso, a API retorna mensagens de confirmação. Exemplo de uma mensagem de sucesso:

- **Mensagem Original em Inglês**: "User registered successfully"
- **Tradução**: "Usuário registrado com sucesso."

Estas mensagens de sucesso são importantes para informar ao usuário ou ao sistema que a solicitação foi processada corretamente.
