#!/bin/sh

/usr/local/bin/locust -f /locust-tasks/locustfile.py  --host=https://jsonplaceholder.typicode.com -u 100 -r 20 --headless --csv=/locust-tasks/demo
