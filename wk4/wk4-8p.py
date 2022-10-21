## Ky Fike, 17 Sep 2022
## 

import string

fhand = open('swift.txt')
line_num = 0
n = 0
word_list = []
occ_list = []
lines_list = []     # The lines where 'word' appear will be stored as a string, so each word in word_list has a corresponding index in lines_list.
for line in fhand:
    line_num += 1
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.strip()
    line = line.lower()
    word = line.split()
    for item in word:
        # print(item)
        if item not in word_list:   # initialize item
            word_list.append(item)
            occ_list.append(1)
            lines_list.append('line(s) ' + str(line_num))
            n = word_list.index(item)
        else:
            n = word_list.index(item)       # this will keep all indices in sync
            occ_list[n] += 1
            lines_list[n] += ', ' + str(line_num)

# We've successfully read in the data. Now the challenge is to sort them and mantain the corresponding indices.
# ^^ Instead, let's just make a new top list of the most frequent words. Then we can access what the word is from
# its occurrence.
top = [max(occ_list)]
size = 20
count = 1
while count < size:
    top.append(0)
    for item in occ_list:
        if top[count] < item < top[count-1]:
           top[count] = item
    count += 1
# print(top)

print("word           number of occurrences\n-----------------------------------")
for item in top:
    n = occ_list.index(item)
    print("%-*s  %s" % (13,word_list[n], item))     # Formatting. Ref: https://www.delftstack.com/howto/python/python-print-column-alignment/


# Word search:
search = True
while search:
    print('\n\nEnter a word to search for: ', end='')
    b = input()
    if b in word_list:
        spot = word_list.index(b)
        print('It is in the list.')
        print(b, 'was used', occ_list[spot], 'times on', lines_list[spot], "\n")
        print('Would you like to search again? enter y/n:')
        s = input()
        if s != 'y':
            search = False
    else:
        print('It is NOT in the list.', "\n")
        print('Would you like to search again? Y/n?')
        s = input()
        if s != 'y':
            search = False