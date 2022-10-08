FROM node:14

ENV front=/home/shlepa/PycharmProjects/pythonProject/farm_front

WORKDIR $front

COPY package*.json ./

RUN npm install
RUN npm install -g @vue/cli
RUN npm install jquery
RUN npm install axios vue-axios —save-dev

COPY . .

EXPOSE 8080

CMD npm run serve