#thread pool
import concurrent.futures
def worker():
    print("Worker thread running")

#Create a thread pool with 2 threads
pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

#submit tasks to the pool
pool.submit(worker)
pool.submit(worker)

#wait for all tasks to complete
pool.shutdown(wait=True)
print("main thread continuing to run")