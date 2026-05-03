import psutil
import asyncio
import time
import aiohttp

BACKEND_URL = "http://api:8000/metrics"
NODE_ID = "node-1"

async def collect_metrics():
    return {
        "node_id": NODE_ID,
        "timestamp": int(time.time()),
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk_io": psutil.disk_io_counters().read_bytes,
        "network_in": psutil.net_io_counters().bytes_recv,
        "network_out": psutil.net_io_counters().bytes_sent
    }

async def send_metrics(session):
    while True:
        data = await collect_metrics()
        try:
            async with session.post(BACKEND_URL, json=data):
                pass
        except Exception as e:
            print("Error:", e)
        await asyncio.sleep(1)

async def main():
    async with aiohttp.ClientSession() as session:
        await send_metrics(session)

asyncio.run(main())