FROM python:3.10.4

WORKDIR /root

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver" ]