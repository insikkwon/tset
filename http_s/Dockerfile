FROM nginx:latest
MAINTAINER insik.kwon 

RUN mkdir -p /etc/letsencrypt/live/tset.ncpkis.com
COPY ./cert/fullchain.pem /etc/letsencrypt/live/tset.ncpkis.com/fullchain.pem
COPY ./cert/privkey.pem /etc/letsencrypt/live/tset.ncpkis.com/privkey.pem
COPY ./cert/options-ssl-nginx.conf /etc/letsencrypt/options-ssl-nginx.conf
COPY ./cert/ssl-dhparams.pem /etc/letsencrypt/ssl-dhparams.pem
COPY ./default /etc/nginx/sites-available/default


CMD ["nginx", "-g", "daemon off;"]
EXPOSE 443
