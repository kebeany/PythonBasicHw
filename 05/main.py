grade = int(input("what grade are you?"))
if grade >= 2 and grade <=4:
    print(' eat hamburger')
else:
    print(' eat pizza')


if grade ==2 or grade ==3 or grade == 4:
    print('eat hamburger')
else:
    print('eat pizza')
pizza = input("is he pizza place open?(yes/no)")
chicken = input("is the chicken place open?(yes/no)")
if pizza == 'yes':
    print('go eat yummy pizza')
elif chicken == 'yes':
    print('go eat chicken')
else:
    print('go eat at 5 guys')


pizza = input("is he pizza place open?(yes/no)")
chicken = input("is the chicken place open?(yes/no)")
seveneleven = input("is seven eleven open? (yes/no)")
if pizza == 'yes':
    print('go eat yummy pizza')
elif chicken == 'yes':
       print('go eat chicken')
elif seveneleven == 'yes':
    print('go to seven eleven')
else:
    print('go eat at 5 guys')
number = int(input("number:"))
if number%2==0:
    print('it is an even number')
else:
    print('it is odd number')
data = input("put in the ticket your going to buy(child/adult):")
if data == ('adult'):
    print("in order for you to get a ticket you will have to pay 5000 won")
else :
    print("in order for you to get a ticket you will have to pay 3000 won")
x = 5
if x!=10:
    print('ok')
num1 = int(input("input number1:"))
num2 = int(input("input number2:"))
num3 = int(input("input number3:"))
if (num1>=num2) and (num1>=num3):
    print(num1)
elif(num2>=num1) and (num2>=num3):
    print(num2)
else:
    print(num3)
idnumber= input("please enter id number: ######-######## format:  ")
if idnumber[7]== "1" or idnumber[7]=="3":
    print("male")
elif idnumber[7] == "2" or idnumber[7]=="4":
    print("female")
else:
    print("error")
score= int(input('grade:'))
if 81<= score:
    print('grade:A')
elif 61<=score:
    print('grade:B')
elif 41<=score:
    print('grade:C')
elif 21<=score:
    print('grade:D')
else:
    print('grade:F')
def print_grade(score):
    if 81<= score:
        print('grade:A')
    elif 61<=score:
        print('grade:B')
    elif 41<=score:
        print('grade:C')
    elif 21<=score:
        print('grade:D')
    else:
        print('grade:F')

score= int(input('grade:'))
print_grade(score)
