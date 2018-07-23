FROM python:2.7

# ENV
ARG PROJ_FOLDER_NAME=cqgcu-enroll-manager
ARG PROJ_NAME=cqgcu-enroll-manager
ENV SERVER_ID container
ENV SERVICE_ID $PROJ_NAME

# set timezone
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install python requirements.txt
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

# install software
RUN pip install uwsgi -i https://pypi.doubanio.com/simple

# copy project files
COPY . /src

# create logs dir
RUN mkdir -p /var/log/cqgcu-enroll-manager/

WORKDIR /src

EXPOSE 80