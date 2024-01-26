# Makefile for building and running Django Docker container

# Variables
CONTAINER_NAME = django-container
DOCKER_IMAGE = django-image
DOCKER_BUILD_CONTEXT = .
HOST_VOLUME = /Users/leetaekwon/Documents/coding/playground/web3.py/djangoServer
CONTAINER_VOLUME = /usr/src/app

WEB_PORT = 8000
RTC_PORT = 7545


.PHONY: build run stop

# Build the Docker image
all : build run

build:
	docker build -t $(DOCKER_IMAGE) $(DOCKER_BUILD_CONTEXT)

# Run the Docker container
run:
	docker run -it -p $(WEB_PORT):$(WEB_PORT) -p $(RTC_PORT):$(RTC_PORT) -v $(HOST_VOLUME):$(CONTAINER_VOLUME)  --name $(CONTAINER_NAME) $(DOCKER_IMAGE) /bin/bash

# Stop and remove the Docker container
clean:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

fclean: clean
	docker rmi $(DOCKER_IMAGE)

re : fclean all

c1 :
	docker exec -it $(CONTAINER_NAME) /bin/bash