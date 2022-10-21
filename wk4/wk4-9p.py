## Ky Fike, 17 Sep 2022
## 

# 9 Program 1
# Create a quiz program for countries and capitals.  There is a helpful file that contains
# countries and capitals.  Create a dictionary where the keys are country and the value is the capital.  

# import random       # randomize the order of quiz questions
# import string       # remove commas from formatting
# print('This quiz is five questions long! Good luck.\n\n')
# fhand = open('country-list.csv')
# quiz_d = dict()
# for line in fhand:
#     line = line.strip('"')
#     words = line.split('","')
#     # 0- country    1-capital   2-type
#     country = words[0]
#     capital = words[1]
#     quiz_d[country] = capital
# # print(quiz_d)  # test dictionary population 
# countries = list(quiz_d.keys())   # create a list of 'country'
# random.shuffle(countries)
# q_size = 5     # this quiz will only be 5 questions long
# c = 0          # counter for quiz size
# rand_abcd = ['a', 'b', 'c', 'd']    # randomly choose which multiple choice option displays the correct capital
# while c < q_size:
#     num = str(c+1)
#     print(num+'. ', end='')     # print question number

#     print('The capital of', countries[c], 'is:')
#     abcd = random.choice(rand_abcd)
#     if abcd == 'a':
#         print('a.', quiz_d[countries[c]], '\nb.', random.choice(countries), '\nc.', random.choice(countries),'\nd.', random.choice(countries))
#     elif abcd == 'b':
#         print('a.', random.choice(countries), '\nb.', quiz_d[countries[c]], '\nc.', random.choice(countries),'\nd.', random.choice(countries))
#     elif abcd == 'c':
#         print('a.', random.choice(countries), '\nb.', random.choice(countries), '\nc.', quiz_d[countries[c]],'\nd.', random.choice(countries))
#     else:
#         print('a.', random.choice(countries), '\nb.', random.choice(countries), '\nc.', random.choice(countries),'\nd.', quiz_d[countries[c]])
#     x = input()
#     if x == abcd:
#         print('Correct!\n')
#     else:
#         print('Incorrect. The capital of', countries[c], 'is', quiz_d[countries[c]],'\n')
#     c += 1


# 9 Program 2

import string

fhand = open('swift.txt')
line_num = 0
n = 0
d = dict()
d_lines = dict()
lines_list = []
for line in fhand:
    line_num += 1
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.strip()
    line = line.lower()
    word = line.split()
    for item in word:
        w = item
        # print(item)
        if w not in d:   # initialize item
            d[w] = 1
            d_lines[w] = ('line(s) ' + str(line_num))
        else:
            d[w] += 1
            d_lines[w] += ', ' + str(line_num)

# Convert the dictionaries back to lists
occ_list = list(d.values())
word_list = list(d.keys())
lines_list = list(d_lines.values())

# Frequency:
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
        print(b, 'was used', occ_list[spot], 'times on', lines_list[spot])
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