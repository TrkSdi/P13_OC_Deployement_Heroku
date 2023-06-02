FROM python:3.10.4

WORKDIR /src

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "-b", "0.0.0.0:8000", "oc_lettings_site.wsgi"]