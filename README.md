# redis-sandbox

Launch redis in docker:
docker run -v /home/samuel/redis-stable/redis.conf:/usr/local/etc/redis/redis.conf -v /home/samuel/redis-stable/crat-redis-db/tc03-07.db:/data/dump.rdb --network="host"  -p 6379:6379 --name myredis redis redis-server /usr/local/etc/redis/redis.conf

Run redis-cli in docker:
docker run -it --network="host" redis redis-cli -h 127.0.0.1  -p 6379:6379
