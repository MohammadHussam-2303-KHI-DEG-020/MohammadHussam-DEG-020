
#!/bin/bash

# commands to create three topics
docker-compose exec broker kafka-topics --create --topic my-first-topic --partitions 3 --bootstrap-server broker:9092
docker-compose exec broker kafka-topics --create --topic my-second-topic --bootstrap-server broker:9092
docker-compose exec broker kafka-topics --create --topic my-third-topic --bootstrap-server broker:9092



#listing the topics 
docker-compose exec broker kafka-topics --list --bootstrap-server broker:9092
