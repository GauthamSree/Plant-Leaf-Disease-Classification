FROM node:16.0.0-slim

COPY . /app/Frontend/

WORKDIR /app/Frontend/

ENV PATH /app/Frontend/node_modules/.bin:$PATH

RUN npm install

CMD ["npm", "start"] 