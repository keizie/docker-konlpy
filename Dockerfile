FROM python:3
RUN [ "pip", "install", "konlpy" ]

RUN apt update && apt install g++ openjdk-8-jdk -y

WORKDIR /opt/konlpy
ADD . /opt/konlpy

COPY komoran.dic /tmp/dic.txt

CMD [ "python3" ]
