#version - anushiya/k8-performance-test:v1
#docker build --no-cache -t anushiya/k8-performance-test:v1 .
#docker push anushiya/k8-performance-test:v1
FROM anushiya/jmeter-plugins:v1

ADD bash /home/kubernetes-performance/bash
ADD jar /home/kubernetes-performance/jar
ADD jmx /home/kubernetes-performance/jmx
ADD python /home/kubernetes-performance/python

WORKDIR /home/kubernetes-performance/bash

RUN chmod +x start_performance_test.sh

RUN apt-get update && apt-get install python3.5 -y
RUN apt-get install python-pip -y
RUN pip install numpy requests schedule objectpath