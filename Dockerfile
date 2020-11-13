FROM ubuntu:18.04
RUN apt-get -y update

RUN apt-get -y install \
      libevent-dev \
      python3.6-dev \
      python3.6 \
      python3-pip \
 && python3.6 -m pip install \
      locust==1.3.2 \
      awscli \
      pandas \
      boto3 \
      xlsxwriter \
      xlrd 
#ADD . /locust-tasks
ADD /PerformenceTests /locust-tasks/PerformenceTests
ADD /run.sh /locust-tasks
WORKDIR /locust-tasks
RUN chmod 755 /locust-tasks/run.sh
RUN chmod 755 /locust-tasks/PerformenceTests/s3-poll.py
EXPOSE 8089 5557 5558
#CMD ["python3","/./PerformenceTests/s3-poll.py"]
#ENTRYPOINT ./run.sh
CMD ["/locust-tasks/run.sh"]
#CMD tail -f /dev/null       
