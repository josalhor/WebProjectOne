# WebProjectOne

This is the project for an assignment for the subject *Web Project*. You can find the main deployment in: https://web-project-one-prod.herokuapp.com

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. Keep in mind during early stages of development we're wiping the database on each run.

### Prerequisites

```
Docker or Docker Toolbox
```

### Run locally on Linux and Mac and Windows with Docker

First of all be logged on docker, otherwise you won't be able to build

```
$ docker-compose up --build --remove-orphans
```

### Run locally on Windows with Docker Toolbox

```
> docker-machine start default &:: Start Virtual Machine
> docker-machine env &:: Configure Terminal
> docker-machine ip default &:: Get IP of machine
> docker-compose up --build --remove-orphans &:: Start Docker/Django
```

### Clean up database

Be very careful with the second command: https://docs.docker.com/engine/reference/commandline/image_prune/

```
docker rm -vf web_project_db
docker image prune -af
```

### Configuration

The server will be deployed on port 80 by default

By default, the local execution runs the file start_server_dev.sh, which configures a default user admin and password only available on local.

Feel free to use `docker-compose exec web` to configure your container, users etc.

You may want to use the file `web.env.secrets.example.sh` and rename it to `web.env.secrets.sh` after adding a NYT API KEY to develop better locally.

## Running the tests locally (without Travis)

```
docker-compose -f docker-compose-test.yml up --build --remove-orphans
```

## Documentation

You can find basic functionality of our site in the DOMAIN.md file.

## Built and deployed with

* [Django](https://www.djangoproject.com/) - The web framework used
* [Docker](https://www.docker.com/) - Container management
* [Heroku](https://www.heroku.com/) - Cloud Application Platform
* [PostgreSQL](https://www.postgresql.org/) - Open Source Database
* [Travis](https://travis-ci.org/) - Test CI - [Also deploys to Heroku with docker](https://travis-ci.org/github/josalhor/WebProjectOne/builds/668481240#L398)
* [Git](https://git-scm.com/) - Version control system
* [GitHub](https://github.com/) - Software development platform
* [django-bootstrap4](https://github.com/zostera/django-bootstrap4) - Django Bootstrap Integration
* [Behave](https://behave.readthedocs.io/en/latest/) - Integration Testing
* [Splinter](https://splinter.readthedocs.io/en/latest/) - Integration Testing

## Authors

- Josep Maria Salvia Hornos
- Balma Cascón Piñol
- Anna Torres Tuca
- Sara Quejido Garriga

### Attribution

Icons made by [Freepik](https://www.flaticon.com/authors/freepik "Freepik") from [www.flaticon.com](https://www.flaticon.com/ "Flaticon")