FROM python:3.8

ENV back=/home/shlepa/PycharmProjects/pythonProject/my_funny_farm

WORKDIR $back

COPY . $back

RUN pip install —upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000