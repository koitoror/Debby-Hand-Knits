FROM python:3.8-alpine

LABEL Daniel Kamar

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --no-cache py3-setuptools

# RUN apk add \
#     build-dep \
#     python-psycopg2 \

RUN apk add --update \
    # py-mysqldb \
    # python-dev \
    postgresql-dev \
    gcc \
    libc-dev \
    mariadb-dev \
    nodejs \
    npm \
    && pip install --upgrade pip  \
    && pip install -r requirements.txt \
    && pip install mysqlclient \
    && pip install psycopg2 \
    && pip install psycopg2-binary \
    && rm -rf /var/cache/apk/*

COPY ./app/package.json /app/package.json

RUN npm install

COPY ./app /app

# PORT=8081

# EXPOSE $PORT
# EXPOSE 8081/tcp

CMD python app.py run -h 0.0.0.0:5000
# CMD ["python", "app.py", "--host", "0.0.0.0"]
# CMD ["python", "add_products.py"]