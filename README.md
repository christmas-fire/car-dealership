# сar-dealership

## Description
This project is a Python-based API that uses PostgreSQL as its database. It is built with FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3 based on standard Python type hints.

## Installation
```
git clone https://github.com/christmas-fire/car-dealership.git
cd car-dealership
```

## Configuration
Replace .env.example with real .env, changing placeholders
```
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=your_postgres_db
POSTGRES_HOST=your_postgres_host
POSTGRES_PORT=your_postgres_port
SECRET_KEY=your_secret_key
ALGORITHM=your_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES=your_ttl
```

## Run with Docker
You must have docker and docker-compose installed on your machine to start this application.

Build and run application.
```
make up
```

Run application without build.
```
make start
```

Stop and remove containers.
```
make down
```

Stop containers without removing.
```
make stop
```

Show application logs.
```
make logs
```

## Documentation
All routes are available in [interactive Swagger documentation](http://localhost:8000/docs#/).