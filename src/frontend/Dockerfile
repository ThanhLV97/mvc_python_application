FROM node:alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "serve", "--", "--host", "0.0.0.0"]
