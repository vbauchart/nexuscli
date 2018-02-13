FROM centos:7

RUN yum install -y python-setuptools

ADD . /src

RUN cd /src && python setup.py install --install-scripts /usr/bin/
