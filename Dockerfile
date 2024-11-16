FROM python:3.9-slim-buster

WORKDIR /app

COPY requirment.txt . 

RUN  pip install --no-cache-dir -r requirment.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0 

EXPOSE 5000

CMD ["flask", "run"]
