FROM ubuntu:18.04

#RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential libncursesw5-dev libreadline-dev libssl-dev libgdbm-dev libc6-dev libsqlite3-dev libxml2-dev libxslt-dev python python-dev python-setuptools && apt-get clean
#RUN easy_install locustio pyzmq
RUN apt-get -y update

RUN apt-get -y install \
      libevent-dev \
      python3.6-dev \
      python3.6 \
      python3-pip \
 && python3.6 -m pip install \
      locust
ADD . /locust-tasks
#ADD /requirements.txt /locust-tasks/requirements.txt
ADD /run.sh /locust-tasks/run.sh
WORKDIR /locust-tasks
RUN chmod 755 /locust-tasks/run.sh
EXPOSE 8089 5557 5558
#CMD ["/usr/local/bin/run.sh"]
#CMD ["locust", "-f", "locust-tasks/locustfile.py", " --host=https://jsonplaceholder.typicode.com", "-u 100", "-r 20", "--no-web", "--csv=demo"]
# locust -f ./locustfile.py --headless -u 1000 -r 100 --csv=demo 
#CMD /usr/local/bin/locust -f /locust-tasks/locustfile.py  --host=https://jsonplaceholder.typicode.com -u 100 -r 20 --headless --csv=/locust-tasks/demo
CMD ["/locust-tasks/run.sh"]
#CMD tail -f /dev/null       
