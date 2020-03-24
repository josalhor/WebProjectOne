# WebProjectOne

This is the project for an assignment for the subject *Web Project*.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

```
Docker or Docker Toolbox
```

### Run locally on Linux and Mac and Windows with Docker

First of all be logged on docker, otherwise you won't be able to build

```
$ docker-compose up --build
```

### Run locally on Windows with Docker Toolbox

```
> docker-machine start default &:: Start Virtual Machine
> docker-machine env &:: Configure Terminal
> docker-machine ip default &:: Get IP of machine
> docker-compose up --build &:: Start Docker/Django
```

### Configuration

The server will be deployed on port 80 by default

By default, the local execution runs the file start_server_dev.sh, which configures a default user and password only available on local.

## Running the tests locally (without Travis)

```
docker build -t joshsalvia/webprojectone -f Dockerfile .
docker run joshsalvia/webprojectone python /app/src/manage.py test
```

## Built and deployed with

* [Django](https://www.djangoproject.com/) - The web framework used
* [Docker](https://www.docker.com/) - Container management
* [Heroku](https://www.heroku.com/) - Cloud Application Platform
* [PostgreSQL](https://www.postgresql.org/) - Open Source Database
* [Travis](https://travis-ci.org/) - Test CI
* [Git](https://git-scm.com/) - Version control system
* [GitHub](https://github.com/) - Software development platform

Authors:
- Josep Maria Salvia Hornos
- Balma Cascón Piñol
- Anna Torres Tuca
- Sara Quejido Garriga
