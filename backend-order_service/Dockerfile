FROM python:3.9-alpine
# FROM python:3.8-alpine

MAINTAINER Daniel Kamar

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add py3-setuptools
# RUN apk add --no-cache py3-setuptools

RUN apk add --update \
     bash \
     curl \
    #  py-mysqldb \
     gcc \
     libc-dev \
     mariadb-dev \
     nodejs \
     npm \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && pip install mysqlclient \
  && rm -rf /var/cache/apk/*

COPY ./app/package.json /app/package.json
RUN npm install

COPY ./app /app

# PORT=8083

EXPOSE $PORT
# EXPOSE 8083/tcp

CMD ["python", "app.py", "--host", "0.0.0.0:$PORT"]

