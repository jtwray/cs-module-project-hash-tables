records = [
    ("Tim", "Austin", "December"),
    ("Jerimiah", "Redmond"),
    ("Paul", "Los Angeles"),
    ("Ryan", "Austin"),
    ("Tucker", "Asheville"),
    ("Ari", "San Jose")
]
​
## How could we show everyone in a given city, in O(1) time?
​
## Treat city as the key
d = {}
​
for record in records:
    city = record[1]
    name = record[0]
    if city in d:
        d[city].add(name)
    else:
        d[city] = set()
        d[city].add(name)
​
print(d["Austin"])
print(d["Redmond"])
​
## we're indexing our records
​
## Checking for membership in a dictionary: O(1)
### a 'get' is O(1)
## Same for set: also based on a hash table
Collapse








