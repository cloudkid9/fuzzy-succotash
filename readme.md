## Introduction

The following script contains common docker commands. The script builds and runs a custom Docker image. Elasticsearch and Kibana containers are created in the script, demonstrating how several Docker containers can be used to replicate a system for testing and development. Further explanation of commands are given inline.

```bash
# Lists out containers running or stopped on the host.
docker ps -a

# Lists out images that are available locally on the host.
docker images

# Creates a non-default docker overlay
docker network create elk

# Creation a Docker image called mypythondocker. Uses the Dockerfile and script in the Dockerfile to create the image. 
docker build -t mypythondocker ./twitter

# Run the previously built docker image. 
docker run -e "name=tim" mypythondocker 

# The following commands pull and run Elasticsearch and Kibana images available from the Dockerhub public repository. 
docker run -d --name elasticsearch --net elk -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "cluster.name=es" elasticsearch:7.5.2

docker run -d --name kibana --net elk --link elasticsearch -p 5601:5601 -e "elasticsearch.hosts=http://es:9200" kibana:7.5.2

# Testing the containers work:
# Check Kibana is running at http://localhost:9200
# Check elasticsearch is healthy
curl http://localhost:9200/_cluster/health

# Stopping a Container
docker stop <container id>

# Starting a Container
docker start <container id>


# Stop and remove all the containers
docker ps -aq | % { docker stop $_ | docker rm $_ }
```

# Elasticsearch 

This script adds data from the JSON file (sample.json) to the Elasticsearch database using the index `bank_accounts`. Refer to inline comments for greater detail.

```bash

# Insert documents from the JSON data file into the Elasticsearch cluster listening on localhost:9200.
curl -H "Content-Type: application/json" -XPOST "localhost:9200/bank_accounts/_bulk?pretty&refresh" --data-binary "@sample.json"

# Inspect indices on the Elasticsearch cluster
curl "localhost:9200/_cat/indices?v"

# Performing a query 
curl -X GET "localhost:9200/bank_accounts/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": { "match_all": {} },
  "sort": [
    { "account_number": "asc" }
  ]
}
'
```

# TODO

- Test Stanford NLP on small text fragments - https://stanfordnlp.github.io/stanfordnlp/
- Test Twitter APIs with twitter python
  1. Update readme with findings