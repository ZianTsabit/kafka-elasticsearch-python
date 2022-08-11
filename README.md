# Data Pipeline Using Kafka, ELK Stack, and Python

## How to Build ?

change ``` KAFKA_ADVERTISED_HOST_NAME ``` in ``` kafka/docker-compose.yaml ``` with your machine IP Address

change ``` bootstrap_servers ``` and ``` hosts ``` in ``` logstash/settings/logstash.conf ``` with your machine IP Address

run ``` sudo docker-compose up -d ``` in each directory

## How to run ?

run ``` sudo docker-compose up ``` in each directory
