for i in [10,20,30]:
    print(i)

for i in [10,20,30]:
    print(i)
    print("-------")

foods = ["sushi","rice","sashimi"]

food = "sushi"
print("today we are going to have:" +food)
food = "rice"
print("today we are going to have:" +food)
food="sashimi"
print("today we are going to have:" + food)

numbers= [3,-20,-3,44]
for i in numbers:
    if i<0:
        print(i)

numbers=(3,100,23,44,103,28,99,65,63,3333)
for i in numbers:
    if i %3==0:
        print(i)

t=(1,2,3,4,5,6,7,8,9,10)
t2=t *10
print(t2)
print(len(t2))

price_list= [1000,2300,9900,15000]
for price in price_list:
    print(price * 1.1)

animals=['dog','cat','parrot']
for animal in animals:
    print(animal)

animals=['dog','cat','parrot','elephant seal']
for animal in animals:
    print(animal[0])

animals=['dog','cat','parrot','elephant seal']
for animal in animals:
    print(len(animal))

numbers=[1,2,3]
for number in numbers:
    print(number*3)

for i in range(2002,2050,4):
    i=i+4
    print(i)

scores=[20,55,67,82,45,33,90,87,100,25]
for i in scores:
    if 50<=i:
        print(i)

scores=[0]*5

for i in range(0,5,1):
    scores[i] = int(input('input {} students grade:'))

for i in range(0,5,1):
    if 60<=scores[i]:
        print('{} this student passed'.format(i+1))
    else:print('{} this student failed')
