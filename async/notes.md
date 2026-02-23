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

## How ClientSession works in aiohttp
1. It creates a connection pool (empty first)
2. session.get(url) checks the pool: If their is any open connection to this host?
3. If no, a new TCP connection (The basic protocol for sending data over the internet) and SSL handshake (the encryption setup for HTTPS) are created.
4. An HTTP req is sent, and we wait for the response headers.
5. The response object holds the connection
6. await response.text() reads the body data from the network   
7. Exit of inner async with loop: The conneciton returns to the pool (stays open).
8. The next req to the same host is made, reusing the connection from the pool
9. Exit outer async with loop: All pooled connections close.

- The connection pool keeps conncetions alive between req. When you make another req to the same host, it skips no 3 step.

- This matters because establishing a new connection is slow. A TCP handshake takes one round-trip to the server. An SSL handshake takes two more. Depending on latency, that's 100-300ms before you even send your first byte of data.

### Using a shared session for all requests

1. BAD Way Fetch in aiohttp
   
```python

# Wrong: new session for each request
async def fetch_bad(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://example.com"] * 10
    results = await asyncio.gather(*[fetch_bad(url) for url in urls])

```
- This creates each new session for per req, which is inefficient. 
- Because the connection should be reused.
- And as they all going to the same host. One should never create a new session.

2. RIGHT way to fetch in aiohttp
```python

# Right: reuse a single session
async def fetch_good(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://example.com"] * 10
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch_good(session, url) for url in urls])

```

- Using the same session/conecction pool.

### Now fetching multiple request sequentailly
```python

import aiohttp
import asyncio
import time

HN_API = "https://hacker-news.firebaseio.com/v0"

async def fetch_story(session, story_id):
    async with session.get(f"{HN_API}/item/{story_id}.json") as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{HN_API}/topstories.json") as response:
            story_ids = await response.json()
        
        start = time.perf_counter()
        stories = []
        for story_id in story_ids[:10]:
            story = await fetch_story(session, story_id)
            stories.append(story)
        elapsed = time.perf_counter() - start
        
        print(f"Sequential: Fetched {len(stories)} stories in {elapsed:.2f} seconds")

asyncio.run(main())

```

### Fetching multiple request concurrently
```python

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{HN_API}/topstories.json") as response:
            story_ids = await response.json()
        
        start = time.perf_counter()
        tasks = [fetch_story(session, story_id) for story_id in story_ids[:10]]
        stories = await asyncio.gather(*tasks)
        elapsed = time.perf_counter() - start
        
        print(f"Concurrent: Fetched {len(stories)} stories in {elapsed:.2f} seconds")
        print("\nTop 3 stories:")
        for story in stories[:3]:
            print(f"  - {story.get('title', 'No title')}")

asyncio.run(main())

```

<!-- Pyton Async Error Handling and Rate Limiting -->

# Rate Limiting

- What happens when you need to fetch 500 stories? or scrape 10,000 pages?
- Most APIs enforce rate limits. They might allow 10 req per second or 100 concurrent conncetions.
- If exceed those limits, you'll get blocked, throttled or banned. 
- Even If API doesn't warn limit, firing thousands of reqs can overwhelm your own system or the server.

- So, for that you need control how many reqs are "in flight" at any moment. That's semaphore does.
  - A semaphore works like a permit system.
  - If you have three permits. Any task that wants to make a request must first obtain a permit.
  - When it finishes, it returns the permit, so a new request can use it.
  - If no permits are available, the task waits until one frees up.
---

![alt text](image.png)

---

- Three permits are available.
- Task A takes a permit (2 remaining), starts its request.
- Task B takes a permit (1 remaining), starts its request.
- Task C takes a permit (0 remaining), starts its request.
- Task D wants a permit, but none are available—it waits.
- Task A finishes, returns its permit (1 available).
- Task D takes that permit and starts its request.
- This continues until all tasks are complete.

- The waiting in step 5 is efficient.
  - It doesn't spin in loop checking "is a permit free yet?".
  - It suspends and let other code run. The evnt loop wakes it only when a permit becomes available.

---
- In asyncio, semaphore is created using asyncio.Semaphore(n), where n is the number of permits.
- Using it, wrap your code in async with semaphore -> This leads to acquire a permit when entering the block and automatically releases it when exiting.

```python

async def fetch_story_limited(session, story_id, semaphore):
    async with semaphore:  # Acquire permit (or wait if none available)
        async with session.get(f"{HN_API}/item/{story_id}.json") as response:
            return await response.json()
    # Permit automatically released here

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{HN_API}/topstories.json") as response:
            story_ids = (await response.json())[:30]

        # Without rate limiting: all 30 at once
        start = time.perf_counter()
        await asyncio.gather(*[fetch_story(session, sid) for sid in story_ids])
        print(f"No limit: {time.perf_counter() - start:.2f}s (30 concurrent)")

        # With Semaphore(5): max 5 at a time
        semaphore = asyncio.Semaphore(5)
        start = time.perf_counter()
        await asyncio.gather(*[fetch_story_limited(session, sid, semaphore) for sid in story_ids])
        print(f"Semaphore(5): {time.perf_counter() - start:.2f}s (5 concurrent)")

asyncio.run(main())
    
```
- This is slow, but good predictable, server-friendly behavior.
- A semaphore limits concurrent requests, not req per time unit.
- Semaphore(10) means "at most 10 requests in flight at once" , not "10 req per second".


### Timeout with asyncio.wait_for()
```python

async def fetch_story_with_timeout(session, story_id, timeout=5.0):
    try:
        coro = fetch_story(session, story_id)
        return await asyncio.wait_for(coro, timeout=timeout)
    except asyncio.TimeoutError:
        return {"error": f"Story {story_id} timed out"}
    finally:
        print("Cleanup complete")  # Runs even on cancellation 
# IF your coroutine holds resources like file handles or connections, use try/finally to ensure cleanup happens even on cancelltion. 
```



