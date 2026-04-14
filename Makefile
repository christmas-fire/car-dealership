DC = docker compose

.PHONY: up
up:
	$(DC) up --build -d 

.PHONY: start
start:
	$(DC) up - d

.PHONY: stop
stop:
	$(DC) stop

.PHONY: down
down:
	$(DC) down

.PHONY: logs
logs:
	$(DC) logs
