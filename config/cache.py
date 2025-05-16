import os
from redis import Redis
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("REDIS_HOST")
port = int(os.getenv("REDIS_PORT"))
password = os.getenv("REDIS_PASSWORD")

# Inicializa la conexion a Redis (Valkey actua como un servidor Redis)
cache = Redis(
    host=host,
    port=port,
    password=password,
    decode_responses=True)

