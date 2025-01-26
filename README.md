# 

## Project structure
An application can consist of multiple modules following this pattern.  

```
Project
├── alembic/
├── src
│   ├── module_1
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
│   ├── config.py  # global configs
│   ├── models.py  # global models (Can be converted into a module if required)
│   ├── exceptions.py  # global exceptions  (Can be converted into a module if required)
│   ├── pagination.py  # global module e.g. pagination
│   ├── database.py  # db connection related stuff
│   └── main.py
├── tests/
│   └── module_1
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── templates/
│   └── index.html
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini
```