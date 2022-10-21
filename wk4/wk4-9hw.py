## Ky Fike, 16 Sep 2022
## 

# 9.1 Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary.
from tkinter import W


fhand = open('words.txt')
the_words = dict()
for line in fhand:
    the_line = line.split() # access each line of the txt file
    for element in the_line:
        the_words[element] = 0 # add each word from the line
# print(the_words)  # test to see if dictionary was populated correctly
print('hi' in the_words)
print('computer' in the_words,'\n')

# 9.2 Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).
fhand = open('mbox-short.txt')
my_dict = dict()
for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        # print(words[2])   # test to double check my_dict output at the end
        if words[2] not in my_dict:
            my_dict[words[2]] = 1
        else:
            my_dict[words[2]] += 1
print(my_dict,'\n')

# 9.3 Write a program to read through a mail log, build a histogram
# using a dictionary to count how many messages have come from
# each email address, and print the dictionary.
fhand = open('mbox-short.txt')
my_dict = dict()
for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        # print(words[1])   # test to double check my_dict output at the end
        if words[1] not in my_dict:
            my_dict[words[1]] = 1
        else:
            my_dict[words[1]] += 1
print(my_dict,'\n')

# 9.4 Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the
# dictionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.

# *include 9.3 code here*
largest = 0
largest_key = None
for key in my_dict:
    if my_dict[key] > largest:
        largest = my_dict[key]
        largest_key = key
print(largest_key, largest,'\n')

# 9.5 This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.
fhand = open('mbox.txt')
my_dict = dict()
for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        # print(words[1])   # test to double check my_dict output at the end
        email = words[1]
        after_at = email.rfind('@') + 1  # +1 so we don't include the at sign
        domain = email[after_at:]     # Slice the string. Ref: David Wright's rfind string method video
        if domain not in my_dict:
            my_dict[domain] = 1
        else:
            my_dict[domain] += 1
print(my_dict,'\n')

# State Capitals:
# Write a program that reads the states_capitols.txt file into a dictionary where the keys
# are the capitals and the states are the values.  Write a program that will randomly quiz
# a user by presenting a capitol and asking the user to type in the state.  
import random       # randomize the order of quiz questions
import string       # remove commas from 'capital, state' formatting
fhand = open('states_capitols.txt')
quiz_date = dict()
for line in fhand:
    line = line.strip()
    words = line.split(', ')
    quiz_date[words[0]] = words[1]
# print(quiz_date)  # test dictionary population - with this test I finally realized my code originally included a '\n' character on the end of every state
capitals = list(quiz_date.keys())   # create a list of 'capitals'
random.shuffle(capitals)
# UNCOMMENT THESE LINES TO RUN THIS PROGRAM:
# for item in capitals:
#     print(item, end=' ')
#     x = input('is the capital of what state? ')
#     # print('x is', x, '\nitem is', item, '\nquiz_date[item] is', quiz_date[item])      # test: trouble shooting
#     if x == quiz_date[item]:
#         print('Correct!')
#     elif x == 'done':
#         break
#     else:
#         print('Wrong!\nIt is the capital of', quiz_date[item])



# Line numbers:
# Write a program that will create a dictionary whose keys are the words in a file.  Create a
# user interface that will allow a user to determine if a word appears in the file and if so
# on what line of the file.  Use TheRaven.txt as a sample file. 
fhand = open('TheRaven.txt')
word_d = dict()
line_num = 0
for line in fhand:
    line_num += 1
    line = line.translate(line.maketrans('', '', string.punctuation)) # this doesn't get rid of all the punctuation! I struggled with separating words like 'there—is'.
    line = line.strip()
    word = line.split()
    for item in word:
        item = item.lower()
        item = item.strip(' ”“—')
        print(item)
        if item not in word_d:
            word_d[item] = 'line(s) 1'
        else:
            word_d[item] += ' ' + str(line_num)
        # print(item)
# print(word_d)
print('Enter a word: ',end='')
w = input()
if w in word_d:
    print(w,'appears on ', word_d[w])
else:
    print(w,"doesn't appear in this file.\n\n")
    

# Encryption:
# Create a dictionary that maps lowercase characters and the space character to some other
# character.  For example, see the encoding.txt file (you may use this if you like).  Use your
# dictionary to encode the text in the file SecretMessage.txt.  Print the encoded message to
# another file.  Then write the program that can decode the message. 
from email import message, message_from_string
import random
import string

iEncrypt = dict()    # I could not find the 'encoding.txt' file. Where is it?
# keyboard smash for each encryption...
iEncrypt['a'] = '0ijfn'
iEncrypt['b'] = '4h254'
iEncrypt['c'] = 'agrfd'
iEncrypt['d'] = 't65as'
iEncrypt['e'] = '3okhf'
iEncrypt['f'] = 'iiwdf'
iEncrypt['g'] = 'SFasv'
iEncrypt['h'] = '0908r'
iEncrypt['i'] = '4df07'
iEncrypt['j'] = 'ig0my'
iEncrypt['k'] = 'asdDa'
iEncrypt['l'] = '>fds<'
iEncrypt['m'] = 'FD465'
iEncrypt['n'] = 'Wjfn9'
iEncrypt['o'] = '#@098'
iEncrypt['p'] = 'words'
iEncrypt['q'] = 'GhfdT'
iEncrypt['r'] = 'L:jjL'
iEncrypt['s'] = 'helo!'
iEncrypt['t'] = 'goodi'
iEncrypt['u'] = '9iull'
iEncrypt['v'] = 'sdd54'
iEncrypt['w'] = 'are45'
iEncrypt['x'] = '33225'
iEncrypt['y'] = 'hhqe3'
iEncrypt['z'] = 'wedsg'
iEncrypt[' '] = '07sfd'
iEncrypt['\n'] = '0;gpd'


the_message = list()
fhand = open('SecretMessage.txt')
for line in fhand:
    line = line.strip()
    line = line.lower()
    for word in line:
        for char in word:
            # print(char)
            the_message.append(iEncrypt[char])
    the_message.append(iEncrypt['\n']) # manually encode newline character when looping to next line
    

ms = str()
for x in the_message:
    ms += x
print(ms)

# write the encrypted message in a new file
with open('EncryptedMessage.txt', 'w') as f:
        f.write(ms)

# reverse the dictionary to decrypt the message
iEncrypt = {v: k for k, v in iEncrypt.items()}      # Ref: https://www.delftstack.com/howto/python/python-invert-a-dictionary/#:~:text=Use%20items()%20to%20Reverse%20a%20Dictionary%20in%20Python,-Python%20dictionaries%20have&text=Reverse%20the%20key%2Dvalue%20pairs,the%20key%20and%20the%20value.&text=The%20k%20and%20v%20in,for%20key%20and%20value%20respectively.
#print(iEncrypt)

# decrypt it - chunking from Ref: https://pythonexamples.org/python-split-string-into-specific-length-chunks/#6
chunks = []
fhand = open('EncryptedMessage.txt')
for line in fhand:
    n = 5
    i = 0
    while i < len(line):
        if i+n < len(line):
            chunks.append(line[i:i+n])
        else:
            chunks.append(line[i:len(line)])
        i += n
#print(chunks)
for item in chunks:
    print(iEncrypt[item],end='')