from redis import Redis

# Inicializa la conexcion a Redis (Valkey actua como un servidor Redis)
cache = Redis(host='localhost', port=6379, db=0, decode_responses=True)
