FROM python:3.10.0b2-alpine3.13
RUN apk add gcc openssl-dev libffi-dev musl-dev

COPY bot.py requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt
RUN chmod a+x /opt/bot.py
WORKDIR /opt/

CMD ["/opt/bot.py"]

