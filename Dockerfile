FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG user

RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev python3-dev musl-dev

RUN adduser -D $user && mkdir -p /etc/sudoers.d \
        && echo "$user ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$user \
        && chmod 0440 /etc/sudoers.d/$user

RUN chown -R $user /usr/local/lib/python3.9/site-packages/ \
    && chmod -R u+w /usr/local/lib/python3.9/site-packages/ \
    && chown -R $user /usr/local/bin/

USER $user

WORKDIR /var/www/app

RUN pip install --upgrade pip
COPY ./requirements.txt .


RUN pip install -r requirements.txt

USER root
RUN apk del .tmp-build-deps

USER $user

COPY . .
