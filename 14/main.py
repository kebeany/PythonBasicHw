f = open("new.txt",'w')

for i in range(1,11):
    data = "this is {} row/rows.\n".format(i)
    f.write(data)

f.close()

f = open("new.txt",'r')

line  = f.readline()
print(line)

f.close()

f = open("new.txt",'r')

while True:
    line = f.readline()
    if not line:
        break 
    print(line)
f.close()

f = open("new.txt",'r')

lines = f.readlines()
for line in lines:
    print(line)

f.close

f = open("new.txt",'r')

data = f.read()
print(data)

f.close()

f = open("new.txt",'w')
f.write("put in new.txt")
f.close()


def print_command():
    print('''    1. icecream added
    2. icecream price
    3. icecream erase
    4. icecream print
    5. stop''')

def print_product(product):
    print('*'*50)
    for key in product.keys():
      print('{} : {}'.format(key, product[key] ))
    print('*'*50)

product = {}
f= open('ICECREAM.txt', 'r')
lines = f.readlines()

for line in lines:
    line = line.rstrip('\n')
    iceCream = line.split(':')
    print(line.split(':'))
    product[iceCream[0]] = iceCream[1]
f.close()

print(product)

while True:
    print_command()
    command = input('pick what you want to do. ')
    if command == '1':
        ice_cream = input('add icecream : ')
        price = input('price : ')
        product[ice_cream] = price
    elif command == '2':
        ice_cream = input('change icecream : ')
        price = input('price : ')
        product[ice_cream] = price
    elif command == '3':
        ice_cream = input(' take out : ')
        del product[ice_cream]
    elif command == '4':
        print_product(product)
    elif command == '5':
        break

f = open("ICECREAM.txt", 'w')

for key in product.keys():
    s = '{}:{}\n'.format(key, product[key])
    f.write(s)

f.close()
