from utils.RabbitMQUtils import get_channel
from aio_pika.abc import AbstractIncomingMessage
from aio_pika import Message
import json
import asyncio


async def SendToRabbit(data: dict):
    channel, queue = await get_channel()
    await channel.default_exchange.publish(
        Message(json.dumps(data).encode()),
        routing_key=queue.name
    )

async def on_message(message: AbstractIncomingMessage) -> None:
    """
    on_message doesn't necessarily have to be defined as async.
    Here it is to show that it's possible.
    """
    print(" [x] Received message %r" % message)
    print("Message body is: %r" % message.body)

    print("Before sleep!")
    await asyncio.sleep(5)  # Represents async I/O operations
    print("After sleep!")

async def GetFromRabbit():
    channel, queue = await get_channel()
    await queue.consume(on_message,no_ack=True)
    await asyncio.Future()
    