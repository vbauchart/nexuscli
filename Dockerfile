FROM centos:7

ENV REGISTRY_URL https://nexus.sys.lab.ingenico.com
ENV REGISTRY_USERNAME svc_nexus_docker
ENV REGISTRY_PASSWORD mypass

RUN yum install -y python-setuptools python-pip && \
    yum clean all

ADD requirements.txt /src/
RUN cat /src/requirements.txt | grep -v setuptools | xargs -i easy_install -U "{}"

ADD nexuscli /src/nexuscli
ADD setup.py  requirements.txt /src/

RUN cd /src && python setup.py install

CMD nexus-cli-docker
