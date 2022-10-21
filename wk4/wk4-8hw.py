## Ky Fike, 9 Sep 2022
## 

# 8.1 Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.
my_list = ['one', 'two', 'three', 'four']
def chop(t):
    del t[0]
    del t[-1]
    return None
val = chop(my_list)
print('chop:', val) # test that val == None

my_list = ['one', 'two', 'three', 'four']
def middle(t):
    del t[0]
    del t[-1]
    return t
val = middle(my_list)
print('middle:', val) # test that val == only middle elements

# 8.2
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        print(words[2])

# 8.3
# ... this is the same as my 8.2 program - with only 1 if statement
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        print(words[2])

# 8.4
unique_words = []
fhand = open('romeo.txt')
for line in fhand:
    this_line = line
    this_line = this_line.split()
    # print(this_line)              # test if this_line is a list
    for element in this_line:
        if element not in unique_words:
            unique_words.append(element)
unique_words.sort()
print(unique_words)

# 8.5 
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        print(words[1])

# 8.6
in_numbers = []
num = input('Enter a number: ')
while num != 'done':
    in_numbers.append(num)
    num = input('Enter a number: ')
print('Maximum:', max(in_numbers))
print('Minimum:', min(in_numbers))