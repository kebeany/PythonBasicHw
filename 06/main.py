number = 0
while number < 10:
    number = number +1
    print(number)

number = 0
max = int(input())
while number<max:
    number = number +1
    print(number)

print("please enter two numbers first with a small number.")
min = int(input())
max = int(input())
while min<= max:
#     print(min)
    min = min +1

print("please enter two numbers first with a small number.")
min = int(input())
max = int(input())
for i in range(min, max +1,1):
    print( i)

max = int(input())
for i in range(1, max +1,3):
    print(i)
max = int(input())
for i in range(5):
    print("hello")
for i in range(1,11):
    print('I took a picture of a tree {} times.'.format(i))
for i in range(3):
    print(i)

i  = 0
while i<3:
    print(i)
    i+=1
number = 0
while number<10:
    number = number + 1
    if number == 5:
        print('{} there is'.format(number))
        break
print(number)

while True:
    data = input('write value:')
    if data == 'input':
        break

number= 2
while number<6:
    number = number +1
    print (number )
    print ("- - - - - - - ")
number = 0
while number < 1000:
    number =number+1
    print(number)

for i in range (1000):
    print (i+1)

for i in range (0,1000,3):
    print (i+1)

number = 0
sum = 0

while number<10:
    number = number +1
    sum = sum + number
    print(number)
    if number == 10:
        print("sum of the numbers are :", format(sum))

number = 0
sum = 0

while number<10:
    number = number +1
    
    print(number)
    if number%2>0:
        sum = sum + number
    elif number == 10:
        print("sum of the odd numbers are :", format(sum))

number = 0
product = 1
while number<10:
    number = number +1
    product = product * number
    print(number)
    if number == 10:
        print("product of the numbers are :", format(product))

i=0
while i<5:
    i=i+1
    print("*" * i)

i=6
while i>1:
    i=i-1
    print("*" * i)

star = int(input("number of stars:"))
i=0
while i< star:
    i=i+1
    print("*" * i)

while True:
    data = int(input('find answer (false or true hint below 60):'))
    if data >= 60:
        print('you pass')
    elif data == range(0,59):
        print('you failed') 
    elif data == -1:
        break
        
while True:
    data = input('what is capital of south korea??') 
    if data == "seoul":
        print('correct')
    elif data =="stop":
        break

while True:
    data = input("give me a number and I will tell if divisible by 7.")
    if data%7==0:
        print("it is divisible by 7")
    elif=-1:
        break
    else:
        print("it is not divisible by 7")

while True :
    data = int(input('what is your score?'))
    if 81<=data:
        print("grade:A")
    elif 61<=data:
        print("grade:B")
    elif 41<=data:
        print("grade:C")
    elif 21<=data:
        print("grade:D")
    elif 0<=data:
        print("grade:E")
    elif -1:
        break


