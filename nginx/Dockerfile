FROM nginx:1.16.1

RUN apt update -y && \
    apt upgrade -y

RUN rm /etc/nginx/conf.d/default.conf
COPY app.conf /etc/nginx/conf.d