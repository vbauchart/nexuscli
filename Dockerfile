FROM centos:7

RUN yum install -y python-setuptools python-pip

ADD requirements.txt /src/
RUN cat /src/requirements.txt | grep -v setuptools | xargs -i easy_install -U "{}"

ADD nexuscli /src/nexuscli
ADD setup.py  requirements.txt /src/

RUN cd /src && python setup.py install --install-scripts /usr/bin/

CMD nexus-cli-docker
