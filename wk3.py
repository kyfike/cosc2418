## Ky Fike, 9 Sep 2022
## 

# 6.1: User input a sentence in which the first letter of each word is capitalized, but there are no spaces between words.
# Parse string and put it in correct format.

str = input('Enter a sentence in which the first letter of each word is capitalized, but there are no spaces between words:\n')

caps = [char for char in str if char.isupper()]      # line ref: https://www.geeksforgeeks.org/python-extract-upper-case-characters/
i = len(caps)

while i > 0:
    str = str.replace(caps[i-1], ' ' + caps[i-1].lower())   # replace capital letters with a space and lowercase
    i = i - 1

str = str.lstrip()  # remove the space at the beginning of the string created in the loop
str = str.capitalize()
print(str)

# 6.2: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number.

str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(':')
#print(colon)              # test: colon position
f = float(str[colon+1:])   # +1 because we don't want to include the colon
print(type(f))             # test: float type

# excercises 7.1 - 7.3 prompts can be found starting on page 101 of http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
# 7.1: 
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
count = 0
for line in fhand:
    line = fhand.readline()
    #line = line.strip()
    print(line.upper(), end='')

# 7.2: 
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

total = 0.0
count = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        num = line[20:]
        num = float(num)                # Never give assign a variable with the name 'float'. This caused me problems for a long time!
        total = total + num
        count = count + 1
print('Average spam confidence: ', (total/count))

# 7.3:
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU!')
        exit()
    print('File cannot be opened: ', fname)
    exit()
