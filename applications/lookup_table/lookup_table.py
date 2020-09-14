# Your code here


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')












# Pattern Matching
​
## Data structures
### Algorithms operate on data
### Consider your data structure: tree, array, hash table?
​
## Time complexity
### Easy to think about with arrays vs hash tables
​
# When to use Hash Tables
​
## Problem they solve: we have something we need to look up quickly
### especially where slower methods would cause a problem
​
my_arr = [1, 2, 3, 4]
my_hash_table = {}
def linear_search(arr, el):
    # check hash table first
    for thing in arr:
        if thing == el:
            my_hash_table[el] = True
            return True
    return False
​
has_3_in_arr = linear_search(my_arr, 3)
​
# million things in arr * million lookups
​
# use hash tables anywhere reacquiring info would be too slow
​



# Memoization
## Dynamic Programming
​
### code up a function
​
### Make a function that will return the n-th element in the Fibonacci sequence
​
### UPER
### Polya's "How to Solve It"
### "run, right, fast"
​
#### Understand
##### ELI5 / Feynman Technique
​
##### Fib sequence?
##### 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
### Agile sprint
### Features --> cards on Kanban board --> "make a button"
​
##### n-th element?
### like in an array
​
#### Plan
##### When you have pseudocode that you can execute
​
### Use a recursive solution (find n-1 and n-2 things)
### Base case
#### 0 and/or 1
### Function calls itself
### Progress toward base case
#### return fib of n-1 and fib of n-2, summed
​
### edge cases: negative numbers and fractions not allowed
​
#### Execute
##### if you discover an edge case or something, throw it in your plan
def fibonacci(n):
    ### Base case
    #### 0 and/or 1
    if n <= 1:
        return n
    ### Progress toward base case
    #### return fib of n-1 and fib of n-2, summed
​
    return fibonacci(n-1) + fibonacci(n-2)
​
#### Review
# fibonacci(3) # should return 2
# fibonacci(2) # should return 1
​
# print(fibonacci(45))
​
#### What is the time complexity of this function?
##### Linear?? only if recursive function calls itself once
##### c^n, c**n, 2^n
​
### Talk about recursion
#### O(1)
#### O(log n)
#### O(n)
#### O(n log n)
#### O(n^c), O(n^2), O(n^3), O(n^4)
#### O(c^n), O(2^n) Exponential
​
### Improve time complexity of our function using memoization
#### make not exponential!
​
​
memo = {}
def memoized_fibonacci(n):
    ### Base case
    #### 0 and/or 1
    if n <= 1:
        return n
​
    ### check if we have a result before doing the computation
    if n in memo:
        return memo[n]
    
    ### store results as we go
    else:
    ### Progress toward base case
    #### return fib of n-1 and fib of n-2, summed
        memo[n] = memoized_fibonacci(n-1) + memoized_fibonacci(n-2)
​
    return memo[n]
​
import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
​
​
# print(memoized_fibonacci(1500))
​
## Tail call recursion
​
​
## Caching
## Lookup tables
## Sorting - can we do it with hash tables?
## Birthday paradox
​
​
​
import math
​
# resize every once in a while
my_arr = []
for i in range(10000):
    my_arr.append(i)
​
# pre-allocating
my_arr = [None] * 10000
for i in range(10000):
    my_arr[i] = i
​
# precalculate the results and cache them in a dict
cache = {}
# kind of an expensive computation
def inverse_root(x):
    return 1/math.sqrt(x)
​
def build_lookup_table():
    for i in range(1, 10000):
        cache[i] = inverse_root(i)
## suppose large numbers, user-facing
## how could we avoid running this computation at time of need?
​
build_lookup_table()
​
## Solves if user asks for a number we have not precalculated
## Populates lookup table
def get_inverse_root(x):
    if x in cache:
        return cache[x]
    else:
        cache[x] = inverse_root(x)
        return cache[x]
​
print(get_inverse_root(9999))
​
print(get_inverse_root(100000))




'''
you set it up before hand because you know this operation is expensivec and you dot want to do it more tahn once at a time. 
hopefully you can have it done already. 
worst case you can do it only once on demand
best case its done already and you just return it

create the dict to look up quickly
define the expensive function

preload the table while you ahve time

write the lookup funciton 
--include a checkfor 
    --if already there return
--include a call to the expensive funciton if not found
    --run once and never have to again
-- you might have to run a scale up to double size of storage
--incorporate some down time for that  

ideal load size of hastable is between 1.2 and 1.4



hashcache= {}

def expensive_function(thing):
    return 0(thing**2(log(thing)))
def build_lookup_table():
    for thing in all_things_list:
            hashcache[thing]=expensive_function(thing)

#run it now beofre user gets to application
#like indexing the tables in a Database

build_lookup_table()




def hashcache_get(thing):
# check hashcache for each thing first
    if think in hashcache:
        return hashcache[thing]
    else:
# add it to the hashcache
        hashcache[thing]=expensive_function(thing)
        returm hashcache[thing]


# on User Click user request
hashcache_get(event.target.state[thing])


'''