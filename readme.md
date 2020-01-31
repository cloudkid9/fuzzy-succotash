

```bash
docker ps 
docker images

# Create a non-default docker overlay
docker network create elk


# Docker making a Docker image 
docker build -t mypythondocker ./twitter

docker run -d --name elasticsearch --net elk -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "cluster.name=es" elasticsearch:7.5.2

# docker pull kibana:7.5.2
docker run -d --name kibana --net elk --link elasticsearch -p 5601:5601 -e "elasticsearch.hosts=http://es:9200" kibana:7.5.2

curl http://localhost:9200

# browser kibana dashboard localhost:5601

docker run -e "name=tim" mypythondocker 


# kill all the containers
docker ps -aq | % { docker stop $_ | docker rm $_ }
```


```bash
curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
  "name": "John Doe"
}
'

curl -H "Content-Type: application/json" -XPOST "localhost:9200/bank_accounts/_bulk?pretty&refresh" --data-binary "@sample.json"

curl "localhost:9200/_cat/indices?v"

curl -X GET "localhost:9200/bank/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": { "match_all": {} },
  "sort": [
    { "account_number": "asc" }
  ]
}
'


```