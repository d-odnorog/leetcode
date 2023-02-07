#!/bin/sh

.PHONY: clean
clean:
	docker stop "$(shell docker ps -aq)"
	docker system prune -f

.PHONY: build-python
build-python:
	docker build -f python/Dockerfile --tag leetcode-python .

.PHONY: run-python
run-python: build-python
	docker run -d -it -v "$(shell pwd)"/python:/app \
	--name my-leetcode-python leetcode-python:latest bash

.PHONY: console-leetcode-python
console-leetcode-python:
	docker exec -it my-leetcode-python bash
