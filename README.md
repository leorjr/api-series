# API REST series

O objetivo desta API é criar um backend simplificado onde podemos realizar um CRUD na mesma, 
nossas series favoritas;

## Features

- Listar todas as series cadastradas;
- Listar series por ID;
- Adicionar uma serie, caso ela não exista;
- Deletar uma série existente, através do seu ID;
- Atualizar uma série existente, através do seu ID;

## ENDPOINTS

Abaixo temos os endpoints para uso desta API:

| Method | EndPoint           | Response                                                                                  | Request Data                                                                                                                         |
| ------ | ------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| GET    | /series                  | Será retornado todas as séries cadastradas no banco de dados                                      | --                                                                                                                                   |
| GET    | /series/<:id>             | Será retornado uma séries especifica, por seu id                                        | --                                                                                                                                   |
| DELETE    | /series/<:id>          | Será deletada uma séries especifica, por seu id                                      | --                    
| PATCH    | /series/<:id>          | Será atualizada uma série, através de seu ID, com os dados passados na requisição                                       | {"genre": str, "imdb_rating": float, "released_date": str, "seasons": int, "serie": str } - Não precisa passar todos os campos                
| POST    | /series | Será criado uma série com os dados passados na requisição | {"genre": str, "imdb_rating": float, "released_date": str, "seasons": int, "serie": str }


## Tech

As principais tecnologias que foram utilizadas neste projeto são:

- Python3;
- Flask;
- PostgreSQL;
- psycopg2-binary;

## Installation

Para rodar este projeto localmente, você deverá entrar na pasta do mesmo:

```
cd api-series
```

Dentro da pasta, você deverá criar uma variável de ambiente (venv) utilizando os seguintes comandos:

```
python -m venv venv
```

Em seguida, deverá ativar o ambiente criado:

```
source venv/bin/activate
```

Em seguida, deverá instalar as dependencias do projeto com o seguinte comando:

```
pip install -r requirements.txt
```

Por fim, para rodar o projeto localmente, deverá dar o seguinte comando:

```
flask run
```

No terminal, será informado o endereço onde você deverá usar no navegador. Geralmente, é o endereço http://127.0.0.1:5000/
