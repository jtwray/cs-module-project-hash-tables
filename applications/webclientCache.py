​
# Make a web client that fetches URLs
## It should cache the results of the call
## On first request, client fetches the web page
## on any subsequent request, client returns from the cache
​
## Why would we make this?
### Speed! don't have to reload the entire page
### So we don't download images etc again
### Fewer network calls - for security
​
### How to use hash tables to make a cache?
### What's the key, what's the value?
​
### What are we given? use as key
### What are we figuring out? use as value
​
## Key: URL
## Value: web page data
​
import requests
import time
​
cache = {}
​
class Cache_Entry:
    def __init__(self, page):
        self.page = page
        self.time_fetched = time.time()
​
​
TIMEOUT = 100
def client_fetch(url):
    if url in cache:
        print('We already have this!')
        cache_entry = cache[url]
​
        if time.time() - cache_entry.time_fetched > TIMEOUT:
            ## Then fetch it again
            pass
​
        return cache[url]
​
    else:
    ## otherwise, go get the url
        data = requests.get(url).text
        ## Change to make into a CacheEntry
        cache[url] = data
        return cache[url]
​
client_fetch('http://www.google.com')
​
## Stale data in the cache
### How to solve?
#### put a timestamp on the cached pages and check the timestamp in the if block
​
## Cache will fill up! use a lot of memory
### LRU cache
### check time_fetched against the 'last-modified' header
​
# Jan 1, 1970