## Ky Fike, 9 Sep 2022
## Chapter 10: Tuples

# Exercise 1
d = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) > 1 and words[0] == 'From':
        if words[1] not in d: 
            d[words[1]] = 1
        else:
            d[words[1]] += 1
# print(d)
tup = tuple()
m = list(sorted(d.values(), reverse=True))    # sort by most messages 
inv_d = {v: k for k, v in d.items()}          
tup = (m[0], inv_d[m[0]])
print(tup[1], tup[0])

# Exercise 2
# This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.
d = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) > 4 and words[0] == 'From':
        t = words[5].split(':')
        h = int(t[0])
        if h not in d: 
            d[h] = 1
        else:
            d[h] += 1
# print(d)  # the dict is still unordered
tup = tuple()
m = list(sorted(d.keys(), reverse=False))    # sort by most messages 
# print(m)
inv_d = {v: k for v, k in d.items()}       
c = 0
for element in m:
    tup = tup + (m[c], inv_d[m[c]])
    print(m[c], inv_d[m[c]])
    c += 1
# print(tup)

# Exercise 3
# Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z.
import string
d = dict()
fhand = open('mbox.txt')
for line in fhand:
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.strip()
    line = line.lower()
    no_nums = ''.join(x for x in line if not x.isdigit())   # remove digits, ref: https://www.studytonight.com/python-howtos/remove-numbers-from-string-in-python
    # print(no_nums)
    words = no_nums.split()
    for item in words:
        for char in item:
            if char not in d: 
                d[char] = 1
            else:
                d[char] += 1
# print(d)  # the dict is still unordered
tup = tuple()
m = list(sorted(d.keys(), reverse=False))    # sort by most messages 
# print(m)
inv_d = {v: k for v, k in d.items()}       
c = 0
for element in m:
    tup = tup + (m[c], inv_d[m[c]])
    print(m[c], inv_d[m[c]])
    c += 1
# print(tup)