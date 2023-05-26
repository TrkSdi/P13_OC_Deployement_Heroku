FROM python:3.10.4

WORKDIR /root

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver" ]