content_array=[]

def file_read(fname):
 
    with open(fname) as f:
        for line in f:
            content_array.append(line)
    f.close()
    return content_array

file_read(ciphertext.txt)

print(content)
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

def letter_counts(s):
    d={}
    for letter in s:
        letter.upper()
        if letter == " ":
            continue
        if letter not in d:
            d[letter]=1
        else:
            d[letter]+=1
    
    return d
def print_letters(s):
    counts_dict=letter_counts(s)
    ##sort by value
    counts_list=list(counts_dict.items())
    counts_list.sort(reverse=True, key = lambda x:x1]) #sort by value in descending order
    

    #loop through and print them
    for pair in counts_list:
        print(f'count:{pair[1]} {letter[0]}')

print_letters(cypher)







# how to use the hash table to make a cache
# whats the key whats the ValueError

# storing webpages by url so we dont have to fetch them more than once


# what are we given use as key
# what are we figuring out use as value


# key"URL
# value: webpage data video images content 











records= [



    ("aarty","dallas"),
    ("alex","austin"),
    ("andy","asheville"),
    ("alvin","dallas"),
    ("amelia","denver"),
    ("amber","dallas"),
    ("anne","denver"),
]





d={}

for record in records:
    city=record[1]
    name=record[0]
    if city in d:
        d[city],add(name)
        else:
            d[city]=set()
            d[city].add(name)
    print(d["dallas"])
    print(d["denver"])














import urllib.requestcache
import requests

cache={}
def client_fetch(url):
    if url in cache:
            print('We already have this!')
            return cache[url]
# otherwise go get the url
    else:
        data=requests.get(url).text
        cache[url] =data
        return cache[url]



        # response = urllib.request.urlopen(url)
        # data= response.read()
        # cache[url] =data
        # return cache[url]

client_fetch('https://google.com')




# gridcache={}
# for cell in grid2dArray:
#   if cell in gridcache:
#       gridcache[cell]+=1
#   else:
#       gridcache[cell]=1 
# 
# 
# 