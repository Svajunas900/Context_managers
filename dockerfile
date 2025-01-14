FROM python:3.10-alpine

WORKDIR /context

COPY requirements.txt /context/

RUN pip install -r requirements.txt

RUN pip install "fastapi[standard]"

COPY . /context/

CMD [ "fastapi", "run", "main.py" ]

EXPOSE 8000

