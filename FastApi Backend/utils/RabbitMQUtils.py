import aio_pika
import json

RABBIT_URL = "amqp://user:password@rabbitmq/"

async def get_channel():
    connection = await aio_pika.connect_robust(RABBIT_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue("metrics", durable=True)
    return channel,queue