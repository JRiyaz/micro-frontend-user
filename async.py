import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import aiohttp
import requests

URL = "http://127.0.0.1:8000/?msg={msg}&sleep={sleep}"
ITEMS_URL = "http://localhost:8000/items/{item_id}"

UUIDS = (
    "76a6668a-b718-4257-a2c9-761888a94d2a",
    "2cb541fb-fc96-4540-a55e-b71234d12bd6",
    "0fca68d2-d1b0-43ad-b2c3-0ab551e8cdbf",
    "25abafe2-b6d1-47f7-8c2f-df9a77a46ac5",
    "ebe08d78-0289-4e6a-80cb-4cd7f7778cd7",
    "4d690669-1e83-4a62-bcef-34d59b689d36",
    "55792b95-9d8f-40ab-9ab0-523df9b5e96a",
    "cbb38574-fcba-449b-81ea-a353c13dfbfd",
    "9409775d-ec74-40c1-af19-18ff040a235c",
    "527ab9d7-e292-474b-b6d0-865d61ad6443",
    "843ad70d-0ebd-4698-aa7b-0a09b6c83429",
    "8143cbe2-9432-4e13-885a-5afd279be7c3",
    "365c61de-af9d-4a7d-a8ae-22f19e634abe",
    "46d9334f-8ce2-4945-a415-30fa7671a643",
    "412e5173-f43b-4113-a20c-b607863c565f",
    "9ad3c18d-2605-4d0d-bff7-890545c5b665",
    "78d44f1f-59d4-4fbf-a5cd-fd2194fe953f",
    "d0cc448f-e9e8-4883-81f1-6310020722bc",
    "087301f5-cb52-49d5-a966-b6ae9f8d418e",
    "09487259-3637-424f-b29e-77ca6a6b2500",
    "85d4b99e-b9dd-4c72-91b7-55ad2173403f",
    "720deb50-0b5a-421b-98ec-2ea235183e29",
    "93e2b31b-eb98-4571-89ab-4adf80845d1f",
    "b2c14e02-2006-4c51-bf43-ab36a2a40661",
    "b61ee497-c290-498c-a6b1-938f9c1d349a",
    "9bcb814a-a8a9-4027-9b3d-47676463fd7a",
    "25066f0a-b6a1-4931-b7ea-0b50375a173c",
    "98ef243a-8bda-41d1-af6d-88970e313061",
    "4b6379ba-03e0-4221-91f7-62aa1feda8f7",
    "2b3af96c-d42b-47ec-bca2-40f8c2e20c9f",
)


async def asynchronous_block(idx: int):
    print(f"{idx}. Thread {threading.current_thread().name} Entered")
    await asyncio.sleep(1)
    msg = f"async-block-{idx}"
    async with aiohttp.ClientSession() as session:
        async with session.get(ITEMS_URL.format(item_id=UUIDS[idx])) as response:
            # request = requests.get(URL.format(msg=f"synchronous-block-{idx}", sleep=5))
            print(f"{msg} block response is {'successful' if response.status == 200 else 'failed'}")
    print(f"{idx}. Thread {threading.current_thread().name} Finished")
    print()
    return None


def synchronous_block(idx: int):
    print(f"{idx}. Thread {threading.current_thread().name} Entered")
    time.sleep(1)
    request = requests.get(URL.format(msg=f"synchronous-block-{idx}", sleep=5))
    print(request.json())
    print(f"{idx}. Thread {threading.current_thread().name} Finished")
    print()


def trigger_synchronous_block():
    print(f"Thread {threading.current_thread().name} started in synchronous_block")
    for i in range(10):
        synchronous_block(idx=i)


def sync_threading_block():
    print(f"Thread {threading.current_thread().name} started in sync_threading_block")
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit 5 tasks to the pool
        futures = [executor.submit(synchronous_block, i) for i in range(10)]
        for future in futures:
            future.result()
            pass


async def asyncio_normal_block():
    # Create tasks correctly, use a list comprehension to create the list of tasks
    tasks = tuple(asyncio.create_task(asynchronous_block(idx=i)) for i in range(30))

    # Wait for all tasks to finish
    await asyncio.gather(*tasks)


async def asyncio_thread_block():
    tasks = tuple(asyncio.to_thread(synchronous_block, i) for i in range(10))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time.perf_counter()
    # trigger_synchronous_block()  # 60.21 seconds with sync-block
    sync_threading_block()  # 6.03 seconds with 10 threads with Sync-block
    # for i in range(100):
    #     asyncio.run(
    #         asyncio_normal_block()
    #     )  # 51 seconds with normal block | 6.02 seconds with aiohttp | 6.05 using to_thread with sync block
    end = time.perf_counter()
    print(f"Time taken to complete: {end - start:.6f} seconds")
