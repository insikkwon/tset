FROM nginx:latest
MAINTAINER insik.kwon 

RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y tcpdump
RUN apt-get install -y net-tools
RUN sed -i 's/Welcome to nginx!/'"$HOSTNAME"'/g' /usr/share/nginx/html/index.html
RUN mkdir -p /etc/letsencrypt/live/tset.ncpkis.com
COPY ./cert/fullchain.pem /etc/letsencrypt/live/tset.ncpkis.com/fullchain.pem
COPY ./cert/privkey.pem /etc/letsencrypt/live/tset.ncpkis.com/privkey.pem
COPY ./cert/options-ssl-nginx.conf /etc/letsencrypt/options-ssl-nginx.conf
COPY ./cert/ssl-dhparams.pem /etc/letsencrypt/ssl-dhparams.pem
COPY ./nginx.conf /etc/nginx/nginx.conf 

CMD ["nginx", "-g", "daemon off;"]
EXPOSE 80 443 8080 8181
