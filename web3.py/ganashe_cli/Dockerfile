# Node.js v14을 기반으로 하는 Docker 이미지를 사용합니다.
FROM node:14

# 작업 디렉토리를 설정합니다.
WORKDIR /usr/src/app

# 애플리케이션에 필요한 npm 패키지들을 설치합니다.
# ganache-cli는 Ethereum RPC client로 사용됩니다.
RUN npm install -g ganache-cli

EXPOSE 8545
# Ganache CLI를 실행합니다.
# -h 0.0.0.0 옵션을 통해 외부에서 접속 가능하게 합니다.
# -p 옵션은 Ganache CLI가 사용할 포트를 설정합니다. 기본값은 8545입니다.

# CMD ["ganache-cli", "-d", "-h", "0.0.0.0", "-p", "8545"]
