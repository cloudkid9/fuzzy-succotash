

```bash
# Create a non-default docker overlay
docker network create elk


# Docker making a Docker image 
docker build -t mypythondocker ./twitter

docker run -d --name elasticsearch --net elk -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "cluster.name=es" elasticsearch:7.5.2

docker run -d --name kibana --net elk --link elasticsearch -p 5601:5601 -e "elasticsearch.hosts=http://es:9200" kibana:7.5.2

curl http://localhost:9200

# browser kibana dashboard localhost:5601

docker run mypthondocker
```


```bash

$JSON = Get-Content -Raw -Path sample.json

$JSON | % { ConvertTo-JSON $_ }