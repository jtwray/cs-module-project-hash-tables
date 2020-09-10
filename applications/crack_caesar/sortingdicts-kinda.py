# Can you sort a hash table?
## No!
## the hash function puts keys at random indices
​
# Do hash tables preserve order?
## NO
## [2, 3, 4, 5]
# my_arr.append(1)
# my_arr.append(2)
# my_arr.append(3)
# [1, 2, 3]
​
# my_hash_table.put(1)
# my_hash_table.put(2)
# my_hash_table.put(3)
​
## *Dictionary
### Yes
### Since Python 3.5, keys are kept in order
### does that impact the time complexity for dict over regular hash tables?
​
### contrast JS: when looping over object items, order is not guaranteed!
#### Means JS object is a little closer to a pure hash table than the Python dict is
​
​
## vim mode and keyboard
​
## Even with a Python dictionary, you can't sort
### We want to print these items, by key, descending order
​
## How could we sort the keys?
d = {
    'foo': 12,
    'bar': 30,
    'quux': 21
     }
​
# use .items() and sort the tuples
# Two common functions/methods for sorting in Python?
## .sort(), sorted(arr)
​
### .items() returns a 'dict_items' object
### can use sorted(), not .sort()...
​
## could use list comprehension
​
## iterable: any data structure you can run a for-loop on
​
my_list = list(d.items())
my_list.sort(reverse=True) # sorts in ascending order, by default. reverse=True to descende instead
my_list.sort(key=lambda tupl: tupl[1]) # sort by value instead of key. optional function argument
​
for pair in my_list:
    print(pair)
​
## JS: (a, b) => a * b
## Python: lambda x, y: x * y
​
my_list.sort(reverse=True, key=lambda tupl: tupl[1]) # sort by value instead of key. optional function argument
for pair in my_list:
    print(pair)
​
## SICP
​
​
## Given a string, print the number of occurrences of each letter
​
## Print starting with the most numerous letter, down to least numerous
​
## Built-in method
# d[letter] = letter.count()
​
string_to_count = "The quick brown fox jumps over the lazy dog"
​
## Store letter as dict key with value of 0, each time the letter appears, increase value by 1
### how to handle spaces?
### upper and lower case?
def letter_counts(s):
    d = {}
    for letter in s:
        letter = letter.lower()
        if letter == " ":
            continue
        elif letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
​
    return d
​
def print_letters(s):
    counts_dict = letter_counts(s)
    ## sort by value
    counts_list = list(counts_dict.items())
    counts_list.sort(reverse = True, key = lambda x: x[1]) # sort by value, and in descending order
​
    ## loop through and print
    for pair in counts_list:
        print(f'count: {pair[1]} letter: {pair[0]}')
​
    
print_letters(string_to_count)
​
## order goes by the order that the data is input if they are the same value
​
​
# named keywords:
def my_func(first_arg, second_arg):
    print(first_arg)
    print(second_arg)
​
my_func(1, 2)
my_func(second_arg=2, first_arg=1)
​
## like kwargs