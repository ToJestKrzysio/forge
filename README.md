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
│   └── main.py  # Application entrypoint
├── tests/
│   └── module_1
├── .env
├── .gitignore
└── alembic.ini
```