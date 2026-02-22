"""

- Before async, Python programs mainly ran in:

A) Synchronous code -> which is called blocking execution.

B) Multithreading:
To improve performance, developers used:
- threading
- multiprocessing

* Threads are expensive => They use more memory.


C) Aysnc Programming
-> Pause a task while waiting for I/O and switch to another task
* main module -> asyncio

"""

# Multithreading example: 
import threading
import time

def task():
    print("Start task")
    time.sleep(3)
    print("End task")

t = threading.Thread(target=task)
t.start()

# aysnc 

    # Coroutine -> A coroutine is a special function defined with:

async def my_function():
    ...

    # It does not run immediately.
    # It returns a coroutine object.

    # await 
        # await tells Python:
        # Pause here until tasks finishes, but let other tasks run meanwwhile.

import asyncio

async def task():
    print("Start task")
    await asyncio.sleep(3)
    print("End task")

asyncio.run(task())

    # asyncio.sleep() is non-blocking -> It does NOT freeze the program


# ============================================== Step by Step ==========================================

# sync version
import time

def task1():
    time.sleep(3)
    print("Task 1 done")

def task2():
    time.sleep(3)
    print("Task 2 done")

task1()
task2() # This takes total 6 seconds

# async version

import asyncio

async def task1():
    await asyncio.sleep(3)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(3)
    print("Task 2 done")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main()) # this takes 3 seconds

# =====================================================

import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    html = await fetch("https://example.com")
    print(f"Fetched {len(html)} characters")

asyncio.run(main())
