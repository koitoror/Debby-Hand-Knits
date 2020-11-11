FROM python:3.8-alpine

MAINTAINER Daniel Kamar

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --no-cache py3-setuptools

RUN apk add --update \
    # py-mysqldb \
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

# PORT=8081

EXPOSE $PORT
# EXPOSE 8081/tcp

CMD ["python", "app.py", "--host", "0.0.0.0"]
CMD ["python", "add_products.py"]