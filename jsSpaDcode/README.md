# single-page-app-vanilla-js

Taken from my YouTube Tutorial:
https://www.youtube.com/watch?v=6BozpmSjk-Y

# node setting with docker

1. docker image pull node:slim 
2. docker run -it -p 3000:3000 -v /Users/tyi/Documents/Practicing/spaDcode/volume:/app node:slim /bin/bash
3. Navigate to the project folder and run the following from a terminal:
   - `npm init -y` (to create a Node.js project)
   - `npm i express` (to install Express)
   - `node server.js` (to run the server)


# django setting with docker


docker run -it -p 3000:3000 -v /Users/tyi/Documents/Practicing/spaDcode/volume_django:/app django:latest /bin/bash

python manage.py migrate
python manage.py migrate
