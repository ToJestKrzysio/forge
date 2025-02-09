# 

## Project structure
An application can consist of multiple modules following this pattern.  

```
Project
├── alembic/
├── data/  # Mount location for docker volumes (for ease of direct access) 
├── envs/  # Env variables for docker containers 
├── src
│   ├── common  # Globaly reusable files
│   │   ├── __init__.py
│   │   ├── config.py  # Global Configuration
│   │   ├── constants.py
│   │   ├── dependencies.py
│   │   ├── exceptions.py
│   │   ├── models.py  # db models
│   │   ├── schemas.py  # pydantic models
│   │   ├── services.py
│   │   └── utils.py
│   ├── module_1  # Some application
│   │   ├── __init__.py
│   │   ├── config.py  # local configuration
│   │   ├── constants.py
│   │   ├── dependencies.py
│   │   ├── exceptions.py
│   │   ├── models.py  # db models
│   │   ├── router.py
│   │   ├── schemas.py  # pydantic models
│   │   ├── services.py
│   │   └── utils.py
│   ├── admin.py # Imports admin UI's which are to be used
│   ├── lifespan.py # Functions handling app start up and teardown
│   └── main.py  # Application entrypoint
├── tests/
│   └── module_1
├── .env
├── .gitignore
└── alembic.ini
```

## Development
For local development using docker  
```shell
cp ./envs/api.default.env ./envs/api.env  # Consider updating variables
cp ./envs/postgres.default.env ./envs/postgress.env # Consider updating variables
docker compose up --build
docker exec --it api alembic upgrade head # To migrate DB to latest version
```

#### Docker-less guide coming in the future (but who cares?)

## Setting new project using template
This template currently contains some boilerplate code which is used to check if all functionalities work correctly, 
some of which should be removed while starting a new project.  
To clean up the project run following
```shell
rm -rf /src/hero
rm -rf /src/example
rm -rf /tests/hero/
```
Then remove line `import src.hero.admin` from `src/admin.py`


