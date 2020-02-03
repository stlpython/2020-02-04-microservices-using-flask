FROM python:3.8

RUN pip install pipenv

WORKDIR /app

COPY . /app

RUN pipenv install

EXPOSE 5000

CMD ["pipenv", "run", "python", "app.py"]