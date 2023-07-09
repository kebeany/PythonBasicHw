#1 
print('\'python\' is a program and language')


#2
temperature1=32
temperature2=32

convert1=(temperature1-32) / 1.8
convert2 = (temperature2*1.8) +32

print(convert1)
print(convert2)

#3
year = 2023

#4
print('Hello world!')
print("Hello world!")
# print(''Hello world!'')#error
# print(""Hello world!"")#error
print('''Hello world!''')
print("""Hello world!""")

sentence = "It is different '10' and 10 in Python"

print(sentence[4]) #s
print(sentence[-6]) #P 
print(sentence[17:19]) #10
print(sentence[10:]) # erent '10' and 10 in Python

#5
s='{} attack!!'
print(s.format(5))# => '5 attack!!'
print(s.format(10))# print(10)
print(s.format(50))# print(50)
print(s.format(297))# print(297)

#6
age = int(input('what\'s your age?'))
year = 2023 - age
print("your age is {} and you were born in {}".format(age,year))


def smile(a):
    return a + ' :D'

a = 'have a nice day'
result = smile(a)
print(result)
 #8
def exchange(won):
    dollar = won/1300
    return dollar

print(exchange(2000))
print(exchange(13000))
print(exchange(1000000))

won = int(input('exchange won to dollar: '))
dollar = exchange(won)
print('you have exchange ${} amount.'.format(dollar))
 #9
a = True #bool
b = False #bool
c = true
d = false
e = TRUE
f = FALSE
 #
x = 4 
y = 9
print(x > y) #false
print(x < y) #true
print(x == y) #false
print(x != y) #true
print(x >= y) #false
print(x <= y) #true
print(x/10 < y) #true

print(10 == 10 and 10 != 5) # true
print(4 > 2 and 7 == 3)#false
print(10 < 5 or 10 > 3)#true
print(9 < 7 or 7 < 3)#false
print(not 10 >= 5)#false
print(not 10 <= 10)#false
 #10
print("1")
if 3 > 7:
    if 10 == 9:
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
 #1
 #4
 #5
 #11
def even_odd(number):
    if number%2==0:
        print('it is even')
    else:
        print('it is odd')

number = input("enter number:")
even_odd(int(number))
 
num1 = int(input("input number1:"))
num2 = int(input("input number2:"))
num3 = int(input("input number3:"))

if num1<num2 and num1<num3:
    print('{} is the smallest number.'.format(num1))
elif num2<num1 and num2<num3:
    print('{} is the smallest number.'.format(num2))
elif num3<num1 and num3<num2:
    print('{} is the smallest number.'.format(num3))
else:
    print('they/some numbers are equal ')
# 12
bus = 40000
ship= 30000
airplane=70000
adult= (bus,ship,airplane)

trip= input("what are you going on to go to busan?(bus,ship,airplane):")
person = input("are you an adult or child?:")

if trip == "bus":
    if person == "child":
        fair=(int(bus)*0.5)
        print("that will be {} for going on the {}.".format(fair,'bus'))
    elif person == "adult":
        fair =(bus) 
        print("that will be {} for going on the {}.".format(fair,'bus'))
    
elif trip == "ship":
    if person == "child":
        fair=(int(ship)*0.5)
        print("that will be {} for going on the {}.".format(fair,'ship'))
    elif person == "adult":
        fair = int(ship) 
        print("that will be {} for going on the {}.".format(fair,'ship'))
    
elif trip == "airplane":
    if person == "child":
        fair=(int(airplane)*0.5)
        print("that will be {} for going on the {}.".format(fair,'airplane'))
    elif person == "adult":
        fair =int(airplane) 
        print("that will be {} for going on the {}.".format(fair,'airplane'))
# 13
for i in range(7,100,7):
    if i:
        print(i)

i = 7 
while i:
    i = i+7
    if i:
        print(i)
# 14
while True:
    capital = input('what is the capital of south korea:')
    if capital == "seoul":
        break
    elif capital:
        print("you are wrong")
# 15
while True:
    score = int(input('what score did you get?:'))
    if score == -1:
        break

    if 81<=score :
        print("you got an A")
    elif 61<=score :
        print("you got a B") 
    elif 41<=score :
        print("you got a C") 
    elif 21<=score :
        print("you got a D") 
    elif 0<=20 :
        print("you got a E")
