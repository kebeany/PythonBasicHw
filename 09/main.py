subject = ['korean','math','english','science']
print(subject)

rainbow = ['red','orange','yellow','green','blue','navy','purple']
first = rainbow[0]
print('first color of the rainbow is {}.'.format(first))

rainbow = ['red','orange','yellow','green','blue','navy','purple']
last = rainbow[6]
print('last color of the rainbow is {}.'.format(last))

animals= ['dog','cat','bird','elphant','bear']
plants=['pine tree','maple','rose','cherry blossom']
wildlife=[animals+plants]
print(wildlife)

animals= ['dog','cat','bird','elphant','pinetree']
animals[4] = 'whale'
print(animals)

animals= ['dog','cat','bird','elphant','whale']
animals.append('humans')
print(animals)

animals= ['dog','cat','bird','elphant','whale']
animals.insert(3, 'pig')
print(animals)

animals= ['dog','cat','bird','elphant','whale']
del animals[1]
print(animals)

animals= ['dog','cat','bird','elphant','whale']
animals.remove('cat')
print(animals)

foods = ('rice','fish','seaweed','kimchi','ramen')
print(foods)

animals= ('dog','cat','bird','elphant','whale')
animals[0] = 'human'
print(animals)

t = (1,2,3,4,5,6,7,8,9,10)
print(t*10)

movies= ['boss baby','avengers','charlie and the chocolate factory','super bad']


movies= ['boss baby','avengers','charlie and the chocolate factory','super bad']
movies.append('frozen2')
print(movies)

movies= ['boss baby','avengers','charlie and the chocolate factory','super bad']
movies.insert(4,'frozen2')
print(movies)

movies= ['boss baby','avengers','charlie and the chocolate factory','super bad']
del movies[1]
print(movies)

movies= ['boss baby','avengers','charlie and the chocolate factory','super bad']
movies.remove('charlie and the chocolate factory')
print(movies)

language1=["c","c++","Java"]
language2= ["pyhton","go","c#"]
languages=language1+language2
print(languages)

movies = ('boss baby','superbad')
movies[0]='super bad' # this will not work because in the code for the movies super bad isn't mentioned.

t=1,2,3,4#tuple

data=int(input("1,2,3: "))
rpc = ("rock", "paper", "scissors.")
if data == 1:
    print (rpc[0])
elif data == 2:
    print (rpc[1])
elif data == 3:
    print (rpc[2])

while True:
    data=int(input("1,2,3: "))
    rpc = ("rock", "paper", "scissors.")
    if data == 1:
        print (rpc[0])
    elif data == 2:
        print (rpc[1])
    elif data == 3:
        print (rpc[2])
    elif data == -1:
        break

meals = []
count=0

while True:
    count=count+1
    meal = input('what would you like to order?(\'type "end if your done ordering):')
    if meal == 'end':
        break
    else:
        meals.append(meal)


order = ('you ordered {}.'.format(meals))
print(order)

scores = []
count=0

while True:
    count=count+1
    score = int(input('what were all of your scores?:'))
    if score == -1:
        break
    else:
        scores.append(score)


finish = ('you finished with {}.'.format(scores))
print(finish)

scores = []
count=0
grade = ('grade A','grade B','grade C','grade D','grade F')
while True:
    count=count+1
    score = int(input('what were all of your scores?:'))
    if 81<=score:
        s=grade[0]
    elif 61<=score:
        s=grade[1]
    elif 41<=score:
        s=grade[2]
    elif 21<=score:
        s=grade[3]
    elif 0<=score:
        s=grade[4]


    if score == -1:
        break
    else:
        scores.append(s)


finish = ('your final grades are {}.'.format(scores))
print(finish)
