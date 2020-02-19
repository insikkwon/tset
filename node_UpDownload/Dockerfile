FROM node:latest
MAINTAINER Insik.Kwon <dubu0226.gmail.com>

RUN apt-get update -y
RUN apt-get install -y vim tcpdump sysstat wget net-tools tar

ADD ./src.tar.gz / 
WORKDIR /src

RUN npm install 
ENV NODE_ENV development
EXPOSE 3000

CMD ["node","index.js"]
