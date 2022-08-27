#Ky Fike, 27 Aug 2022

#p1
name=input('What is your name? ')
print('Hello, %s'%name)

#p2
num = int(input('Enter a number: '))
print(type(num))

if num%2==0:
    print("%d is even!"%num)
else:
    print("%d is odd!"%num)


#p3
tempC=int(input('Enter a temperature in Celsius: '))
tempF=9/5*tempC+32
print('That is approximately %i degrees in Fahrenheit'%tempF)