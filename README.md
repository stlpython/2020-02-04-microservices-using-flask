# Microservices in Flask

STL Python talk given on 2/4/2020

## Running slides

_Requires Python 3.8+ & pipenv installed_

```
pipenv install
pipenv run jupyter notebook slides.ipynb
```

## Running the example app

_Requires docker and docker-compose_

If you have a loggly account setup, you can add your client key to the `docker-compose.yml` file's `LOGGING_KEY` environment variables to capture logs

```
docker-compose up --build
```