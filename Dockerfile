FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
RUN ls
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt