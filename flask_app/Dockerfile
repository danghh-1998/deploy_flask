FROM continuumio/anaconda3:latest

LABEL author.name = "Hoang Hai Dang"
LABEL author.email = "hoanghaidang1998@gmail.com"

RUN apt update -y && \
    apt upgrade -y

RUN pip install flask flask_sqlalchemy gunicorn

ADD . /workspace

WORKDIR /workspace

RUN chmod a+x /workspace/*

ENTRYPOINT ["/workspace/entrypoint.sh"]

EXPOSE 80
