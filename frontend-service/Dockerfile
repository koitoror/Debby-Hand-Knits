FROM python:3-alpine

MAINTAINER Daniel Kamar

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY ./app /app

# PORT=8080

EXPOSE $PORT
# EXPOSE 80/tcp

CMD python app.py run -h 0.0.0.0:$PORT

# CMD ["python", "app.py", "--host", "0.0.0.0"]
