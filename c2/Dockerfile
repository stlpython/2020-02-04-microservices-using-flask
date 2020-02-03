FROM python:3.8

RUN pip install pipenv

RUN pipenv install 

EXPOSE 5001

CMD ["pipenv", "run", "python", "app.py"]