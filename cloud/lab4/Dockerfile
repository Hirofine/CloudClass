FROM ubuntu/apache2

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt update

RUN apt install -y python3
RUN apt install -y pip

RUN pip install -r requirements.txt

COPY . ./
COPY user_interface/* /var/www/html/
EXPOSE 80 

ENTRYPOINT ["python3", "./tutorial/Books/manage.py", "runserver", "0.0.0.0:8000"]

