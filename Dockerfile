FROM python:3.10

RUN mkdir /cluddy-train

WORKDIR /cluddy-train

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python3 main.py