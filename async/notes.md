# ASYNC PROGRAMMING

## Python's async system uses a few core concepts:

- Coroutines: Functions defined with async def instead of def. They can pause and resume execution, making them perfect for operations that involve waiting.

- await: This keyword tells Python, "pause this coroutine until this operation completes, but let other code run in the meantime."

- Event loop: The engine that manages all your coroutines, deciding which one to run and when to switch between them.

- Tasks: Coroutines wrapped for concurrent execution. You create them with asyncio.create_task() to run multiple operations at once.


## What async programming can (and can’t) do:

1. Async works best with I/O-bound work like HTTP requests, database queries, and file operations, where your code waits for external systems.

2. Async doesn't help with CPU-bound work such as complex calculations or data processing, where your code actively computes rather than waits.


## Implementation

```python

import asyncio

async def greet_after_delay():
    print("Starting...")
    await asyncio.sleep(2)  # Pauses, but doesn't block
    print("Hello!")

asyncio.run(greet_after_delay()) # starts the event loop and runs the coroutine.

```
- Every async function must be called with await.
- Whether it's a built-in like asyncio.sleep() or one you write yourself, forgetting await means it won't actually execute.
  
<!-- Important -->
- You can't call an async function directly like a regualr function 
- If you do, This returns:
    - `<coroutine object greet_after_delay at 0x...>`
    - `<class 'coroutine'>`
- Calling any async function returns a coroutine object, not the result.
- You need asyncio.run() or await to execute it inside another function.

<!-- How event loop worrks -->

## How Event Loop Works
- Event loop is the engine behind async programming
  1. asyncio.run() creates an event loop.
  2. Event loop starts greet_after_delay().
  3. "Starting..." prints.
  4. Hits await asyncio.sleep(2) → coroutine pauses.
  5. Event loop checks: "Any other tasks to run?" (none right now).
  6. 2 seconds pass, sleep completes.
  7. Event loop resumes greet_after_delay().
  8. "Hello!" prints.
  9. Function finishes → event loop exits.

- With one coroutine, there's nothing else to do. 
- But when you have multiple coroutines, the event loop switches to other work while one waits. 
- Instead of sitting idle during a two-second sleep, it can run other code.

```python 

async def main():
    message = await get_message()
    print(message)

asyncio.run(main())

```

### Why sequential await is still sequential

- If you call it like this:
```python
import asyncio
import time

async def greet_after_delay(name):
    print(f"Starting {name}...")
    await asyncio.sleep(2)
    print(f"Hello, {name}!")

async def main():
    start = time.perf_counter()
    
    await greet_after_delay("Alice")
    await greet_after_delay("Bob")
    await greet_after_delay("Charlie")
    
    elapsed = time.perf_counter() - start
    print(f"Total time: {elapsed:.2f} seconds")

asyncio.run(main())

```
- This will still run sequentially with async because, each await waits fot its coroutine to finish before moving to the next line.

- To run that concurrently:

### Use asyncio.gather()
- This takes multiple coroutines and run them together/concurrently
```python

async def main():
    start = time.perf_counter()
    
    await asyncio.gather(
        greet_after_delay("Alice"),
        greet_after_delay("Bob"),
        greet_after_delay("Charlie"),
    )
    
    elapsed = time.perf_counter() - start
    print(f"Total time: {elapsed:.2f} seconds")

asyncio.run(main())

```
- asyncio.gather() returns a list of results in the same order you passed the coroutines. If your coroutines return values, you can capture them.

```python

async def fetch_number(n):
    await asyncio.sleep(1)
    return n * 10

async def main():
    results = await asyncio.gather(
        fetch_number(1),
        fetch_number(2),
        fetch_number(3),
    )
    print(results)

asyncio.run(main())

```
- This gives [10,20,30] as results

<!-- ============================= aiohttp ================================ -->

# aiohttp
- requests lib is synchronous and blocks the event loop and defeats the purpose of async.
- Instead use aiohttp, an async HTTP client built for this purpose.

### Fetching a URL
```python

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

```

### What does context manager mean? And what is the use of `aysnc with`
- Context manager in Python is an object that defines a temporary runtime environment for a block of code, automatically handling resource allocation and deallocation (setup and cleanup operations).
  
- This ensures that resources are properly acquired and released, even if an exception occurs during the code execution within the defined context.
  
- Context managers are primarily used with the with statement and serve to replace verbose try...finally blocks, resulting in cleaner, safer, and more readable code. 
  
- Automatic resource management -> Guarantee cleanup actions such as closing files, relasing network connections or unlocking resources are performed every time the with block is exited.

1. What does normal with does?
```python

with open("file.txt") as f:
    data = f.read()

```
What happens:
- __enter__() runs

- Block executes

- __exit__() runs (even if error happens)
This guarantees cleanup.


2. Why normal with is NOT enough for async:
   1. While working with:
      1. network connections
      2. database connections
      3. HTTP sessions
      4. sockets
   2. These oftens needs async cleanup:
      1. waiting for buffers to flush
      2. closing connections properly
      3. waiting for remote ACK
- Cleanup might requries await.
- `async wait`

3. What async with really does:
   1. Instead of __enter__ & __exit__
   2. Async context manager define => __aenter__ & __aexit__
   3. These are coroutines

4. So Internally:
   1. `async with something:`
means:
```python
obj = something
value = await obj.__aenter__()
try:
    ...
finally:
    await obj.__aexit__()
```

## How fetching with URL code works?

1️⃣ async def fetch :
- Marks the function as a coroutine so it can use await and run inside the event loop.

2️⃣ First async with ClientSession() : 
- Opens and safely closes the HTTP session (connection pool, sockets).

3️⃣ Second async with session.get(url) : 
- Opens and safely closes the individual HTTP request/response.

Why twice?
- You are managing two separate async resources:
    - The session
    - The response
- Each needs async setup + async cleanup → so each needs its own async with.

In short : 
1. An async def function only makes the function body asynchronous.

2. It does not automatically handle resource setup and cleanup safely.

3. async with guarantees that __aenter__ and __aexit__ are awaited properly, even if an error occurs.

4. So async def defines async code, but async with safely manages async resources.
