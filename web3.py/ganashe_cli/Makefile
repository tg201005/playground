.PHONY: build run clean fclean re

# Docker 이미지 이름입니다.
IMAGE_NAME = ganache-cli

# Docker 컨테이너 이름입니다.
CONTAINER_NAME = ganache-cli-container

# Docker 컨테이너를 실행할 때 연결할 포트입니다할
PORT = 8545

#all
all: build run

# Docker 이미지를 빌드하는 명령입니다.
build:
	docker build -t $(IMAGE_NAME) .

# Docker 컨테이너를 실행하는 명령입니다.
run:
	docker run -d -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME) /bin/bash

# Docker 컨테이너를 중지하고 삭제하는 명령입니다.
clean:
	docker stop $(CONTAINER_NAME) && docker rm $(CONTAINER_NAME)

exec:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# Docker 이미지를 삭제하는 명령입니다.
fclean: clean
	docker rmi $(IMAGE_NAME)

re: fclean all