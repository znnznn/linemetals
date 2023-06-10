FROM python:3.11-slim-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

#RUN chmod +x ./entrypoint.sh

ENV ACCEPT_EULA=Y

RUN apt-get update &&  \
    apt-get upgrade -y && \
    apt-get install -y  \
        curl \
        libpq-dev \
        gnupg \
        gcc \
        g++ &&\
    sh -c "curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -" &&\
    sh -c "curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list" &&\
    apt-get update && \
    apt-get install -y \
        msodbcsql17 \
        mssql-tools \
        libpython3-dev \
        libgssapi-krb5-2 \
        unixodbc-dev \
        unixodbc &&\
    # install application requirements
    python -m pip install --upgrade pip &&\
    pip install pipenv && \
    PIPENV_VENV_IN_PROJECT=1 pipenv install --system
