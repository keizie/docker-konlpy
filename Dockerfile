FROM python:3
RUN [ "pip", "install", "konlpy" ]

RUN apt update && apt install g++ openjdk-11-jre-headless -y

WORKDIR /opt/konlpy
ADD . /opt/konlpy

COPY komoran.dic /tmp/dic.txt

CMD [ "python3", "main.py" ]
