FROM ubuntu/apache2:2.4-21.10_beta

COPY requirements.txt /app/requirements.txt

WORKDIR /app

#RUN pip install -r requirements.txt

COPY . ./
COPY . /var/www/html/




#ENTRYPOINT ["python3", "./tutorial/Books/manage.py", "runserver", "0.0.0.0:8000"]

