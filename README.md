# Line metals API

## Tech details

|         **Resource**          |  **Resource Name**   | **Version** |       **Comment**       |
|:-----------------------------:|:--------------------:|:-----------:|:-----------------------:|
| Back-end programming language |        python        |    3.11     |                         |
|    Back-end web framework     |        Django        |     4.2     |          + DRF          |
|           Database            | Microsoft SQL Server |             | mirror origin db tables |
|          Web server           |        Dafne         |             |    will be gunicorn     |

## Installation & Lunch

## Run command with docker

Run project with docker.
You need install docker
need set environments

```commandline
docker-compose up --build
```

# After docker run app has 2 containers:

- WEB
- DB

## Run commands

Needs add environments vars

|             **PARTH**             |                     **Commands**                      |              **Description**               |
|:---------------------------------:|:-----------------------------------------------------:|:------------------------------------------:|
|           Requirements            |                  pip install pipenv                   |                                            |
|           Requirements            |                    pipenv install                     |    this installed dependencies to venv     |
|        Start django server        |              python3 manage.py runserver              |          <http://127.0.0.1:8000/>          |
|            Stop server            |                       ctrl + C                        |                                            |
| Run migrations or database schema |               python3 manage.py migrate               |                                            |
|             Run seeds             |                                                       |                                            |

## Dev environment deployment

Populate `Environment variables` of your system with the following:

```bash
export DEBUG # default False
export SECRET_KEY

export DJANGO_SETTINGS_MODULE="linemetals_api.settings"

export DATABASE_NAME
export DATABASE_USER
export MSSQL_SA_PASSWORD
export DATABASE_HOST
export DATABASE_PORT=1433

export ACCEPT_EULA=Y # for Microsoft SQL engine
```

Then install all the required packages:

```bash
user@host$ cd linesmetal/
```

```bash
user@host$ pip install pipenv
user@host$ pipenv install
user@host$ ./manage.py runserver
```
