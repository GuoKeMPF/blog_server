FROM centos:7
FROM python:3.11.4


WORKDIR /blog_server
ENV PYTHONUNBUFFERED 1
COPY ./ ./
RUN pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple/
RUN pip install --upgrade pip --default-timeout=100
RUN pip install -r ./requirements.txt
RUN chmod +777 start.sh
EXPOSE 8000
CMD ["/bin/sh","start.sh"]