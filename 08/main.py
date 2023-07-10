s=0
while s<1000:
    s=s+1
    print(s)

for i in range(0,1000,1):
    i=i+1
    print(i) 

sum=0
total=0
for sum in range(0,10,1):
    sum=sum+1
    total = total + sum
    print(total)

sum=0
total=0
for sum in range(0,10,2):
    sum=sum+1
    total = total + sum
    print(total)

sum=0
total=1
for sum in range(0,10,1):
    sum=sum+1
    total = total * sum
    print(total)

for i in range(0,6,1):
    print('*' * i)

for i in range(6,0,-1):
    print('*' * i)

s=int(input("how many stars?:"))
for i in range(0,s,1):
    print('*' * i)

while True:
    s = int(input("guess number:"))
    if s == -1:
        break
    elif 61<=s:
        print("pass")
    elif 60>= s:
        print("fail")

while True:
    cap=input("what is the capital of south korea?:")
    if cap=='stop':
        break
    elif 'seoul' == cap:
        print('correct')
    else:
        print('NOPE')

s = int(input("give me a number and I will tell you if divisible by 7:"))
if (s%7>0):
    print("this is not divisible by 7")
else:
    print("this is divisible by 7")

while True:
    score = int(input("what score did you get?:"))
    if score == -1:
        break


    if 81<=score:
        print('grade A')
    elif 61 <= score:
        print('grade B')
    elif 41<=score:
        print('grade C')
    elif 21 <= score:
        print('grade D')
    else:
        print('grade F')

while True:
    for x in range(0,10,2):
        x=x+1
        print(x)
    for s in range(0 ,10,2):
        print(s)
    for y in range(0,13,3):
        print(y)
    break

import random

print('your given 2 numbers between 0-100. Find the sum.')

num1=random.randint(0,100)
num2=random.randint(0,100)

print('num1 :{0}, num2 : {1}'.format(num1,num2))

answer = num1+num2
count=0
while True:
    count+=1
    print("This is your answer #{} attempt".format(count))
    user = int(input('what is the sum of the numbers?'))
    if user>answer:
        print("too much")
    elif user<answer:
        print("too little")
    else:
        print("correct")
        break

import random
count = 0 

import random
count = 0 

while True:
  print('-------------------------------------------')
  player = input('rock,paper,scissors: ')
  if player == 'stop':
        break
       
  com = random.randint(1, 3)
  if com == 1:
     com = 'rock'
  elif com == 2:
     com = 'paper'
  elif com==3:
     com = 'scissors'

  print('user ( {} vs {} ) computer'.format(player, com))

  if player == 'scissors' or player == 'paper' or player == 'rock' :
        if (com == 'scissors' and player == 'paper') or (com == 'rock' and player == 'scissors') or (com == 'paper' and player == 'rock') :
            print('computer wins')
        elif (player == 'scissors' and com == 'paper') or (player == 'rock' and com == 'scissors') or (player == 'paper' and com == 'rock') :
            print('player wins')
            count = count+1 
            print('count : {}'.format(count))
            if count == 3:
                print("player won 3 times.")
                break
        elif player== ('scissors' and com == 'scissors') or (player == 'paper' and com =='paper') or (player == 'rock' and com =='rock'):
            print('we tied') 


  else:
      print("잘못 입력했습니다.")
      continue
  

            
