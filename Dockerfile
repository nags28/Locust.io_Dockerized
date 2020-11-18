FROM ubuntu:18.04
RUN apt-get -y update

RUN apt-get -y install \
      libevent-dev \
      python3.6-dev \
      python3.6 \
      python3-pip \
 && python3.6 -m pip install \
      locust
ADD . /locust-tasks
ADD /run.sh /locust-tasks/run.sh
WORKDIR /locust-tasks
RUN chmod 755 /locust-tasks/run.sh
EXPOSE 8089 5557 5558
CMD ["/locust-tasks/run.sh"]
#CMD tail -f /dev/null       
