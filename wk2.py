## Ky Fike, 1 Sep 2022
## Loops. Conditionals. Import random, import math.

#--------------- below this line is practice code for testing ideas

# inNum = input('Enter a numerator: ')
# num = int(inNum)
# inDen = input('Enter a denominator: ')
# den = int(inDen)
# try:
#     result = num/den
#     print(result)
# except:
#     print('Error: tried to divide by zero.')

# k = int(input('Enter a guess between 1-10: '))
# k != 0 and k != 1 and k != 2 and k != 3 and k != 4 and k != 5 and k != 8 and k != 9

# ans = int('347')
# print(type(ans))
# print(ans)
# ans = int(999.999)
# print(type(ans))
# print(ans)
# ans = float(45)
# print(type(ans))
# print(ans)
# ans = float('900.45')
# print(type(ans))
# print(ans)

# area of a circle:
# import math
# radius = float(input('Enter the radius of a circle: '))
# area = math.pi*math.pow(radius, 2)
# print('The area of the circle is %f.'%area)

# sqrt(cos2(x) + sin2(x))
# import math
# x = float(input("Enter a value for x: "))
# answer = math.sqrt(math.pow(math.cos(x), 2) + math.pow(math.sin(x), 2))
# print(answer)

# Find random numbers
# import random
# print(random.randint(105,210))

# import random
# nums = [5, 7, 10, 20, 67]
# print(random.choice(nums))

# import random
# print(random.uniform(10, 19.9999999999999999))

# x = range(4, 17, 3)
# print(list(x))
#--------------- above this line is practice code for testing ideas^^


# p3: classifying plants: algae, moss, fern, angiosperm monocot, angiosperm dicot, gymnosperm
vascular = int(input('\nEnter "1" if the statement is true to determine what plant kingdom your plant belongs to. Enter any digit other "1" if the statement is false. \nThe plant...\npossesses true stems, roots, and leaves? '))
if vascular == 1:
    seeds = int(input('\nproduces seeds? '))
    if seeds == 1:
        flowers = int(input('\nproduces flowers? '))
        if flowers == 1:
            angiosperm = int(input('\nhas a one seed leaf? '))
            if angiosperm:
                print('It is an angiosperm monocot.')
            else:
                print('It is an angiosperm dicot.')
        else:
            print('It is a gymnosperm.')
    else:
        print('It is a fern.')
else:
    moss = int(input('\nhas structures that look like a root, stem or leaf? '))
    if moss == 1:
        print('It is moss!')
    else:
        print('It is algae.')

# p4.1: Write a function that can compute and return the area of a circle. Test it in main().
import math
def area(radius):
 result = math.pi*math.pow(radius, 2)
 print(result)

radius = float(input('Enter the radius of the circle: '))
area(radius)

# p4.2: Get an integer from the user, and don't crash or end the program until you succeed. (With help from https://www.101computing.net/number-only/)
def getInt():
 wantedType = False
 while wantedType == False:
  x = input('Enter an integer: ')
  try:
   x = int(x)
   wantedType = True
  except ValueError:
   print('That is not an integer!')

getInt()

#p5.1: Re-write the code example in 5.3 so that break is not needed. 
line = input('> ')
while line != 'done':
    print(line)
    line = input('> ')
print('Done!')

#p5.3: 
def getInt(x):
 wantedType = False
 while wantedType == False:
  try:
   x = int(x)
   wantedType = True
   return x
  except ValueError:
   print('Error! ', end='')
   x = input('Try entering an integer: ')

def getFloat(x):
 wantedType = False
 while wantedType == False:
  try:
   x = float(x)
   wantedType = True
   return x
  except ValueError:
   print('Error! ', end='')
   x = input('Try entering a floating point number: ')


popSize = input('Enter the population size: ')
popSize = getInt(popSize)
# print('this is the popSize: %i' %popSize)     # test-line
gR = input('Enter the growth rate: ')
gR = getFloat(gR)
days = input('Enter the number of days: ')
days = getInt(days)

newPop = popSize + popSize * gR

for i in range(1, days+1):
  print('After day',i,',the new population will be:',newPop)
  newPop = newPop + newPop * gR         # use newPop for further calculations, not the original popSize








# access the 7th slice of the string
print(x[6])
print('\n')

# change the sep to ',' (maxNumSplits is still default)
x = str.split(',')
print(x)
print('\n')



# csv file example
line = '"82601","43.0655","-106.34618","Casper","WY","Wyoming","TRUE","","26854","21.7","56025","Natrona","{""56025"": 100}","Natrona","56025","FALSE","FALSE","America/Denver"'
lineSplit = line.split('","')
city = lineSplit[3]
state = lineSplit[4]
print(city, ', ' ,state, sep='')
print('\n')
