dic= {}
print(dic)

user= { 'name':'Jimmy','yearsold':150,'gender':'male','born' :1873}
print(user)

icecream = {"돼지바": 1200, "죠스바": 1000, "보석바": 1800}
print(icecream)

icecream = {"돼지바": 1200, "죠스바": 1000, "보석바": 1800}
icecream["vanila icecream"]=1000
icecream["chocolate icecream"] = 1000
print(icecream)

icecream = {"돼지바": 1200, "죠스바": 1000, "보석바": 1800}
print("돼지바:",icecream["돼지바"])

icecream = {"돼지바": 1200, "죠스바": 1000, "보석바": 1800}
icecream["돼지바"]=1300
print(icecream)
icecream = {"돼지바": 1200, "죠스바": 1000, "보석바": 1800}
del icecream["돼지바"]

print(icecream)

name={'name':"돼지바",'name':"죠스바",'name':"보석바"}
icecream = {"돼지바": [1200,25], "죠스바": [1000,32], "보석바": [1800,43]}
print(icecream)
print(name)

icecream = {"돼지바": [1200,20], "죠스바": [1000 ,3], "보석바": [1800,100]}
icecream ["worldcone"] = [500,7]
print(icecream)

icecream = {"돼지바" : 1200, "죠스바" : 1000, "보석바" : 1800}
print(icecream.keys())

for key in icecream.keys():
    print(key, icecream[key])

icecream = {"돼지바" : 1200, "죠스바" : 1000, "보석바" : 1800}
print(icecream.keys())

for key in icecream.keys():

    if 1200<=icecream[key]:
        print(icecream[key])

icecream = {"돼지바": 1200, "죠스바": 1000, "보석바": 1800}
print(icecream.values)

for price in icecream.values():
    print(price)

icecream = {"돼지바": 1200, "죠스바": 1000, "보석바": 1800}
print(icecream.items())

for key,value in icecream.items():
    print(f'{key} : {value} ')

icecream = {"돼지바": 1200, "죠스바": 1000, "보석바": 1800}
icecream.clear()
print(icecream)

icecream = {"돼지바": 1200, "죠스바": 1000, "보석바": 1800}
print(icecream.get("돼지바"))
print(icecream.get('vanilla'))

icecream.get("돼지바",'vanilla')

icecream = {"돼지바": 1200, "죠스바": 1000, "보석바": 1800}
print("돼지바" in icecream)
print('vanila' in icecream)


a=[1,1,1,2,2,3,3,3,4,4,5]
s=set(a)
print(s)

a= {2,1,3,5,7}
b= {3,4,1,6}
print(a&b)

a = {2,1,3,5,7}
b = {3,4,1,6}
print(a-b)

a = {2,1,3,5,7}
b = {3,4,1,6}
print(b-a)

dic1 = {'key': 'value'}
dic2 = {1: ['hello']}
dic3 = ['철수', ':', '영희']
dic4 = {'1', '2', '3'}
dic5 = ('사과', ':', 'apple')
dic6 = 'age : 12'
dic7 = 100.2
dic8 = {'김밥':3000, '떡볶이':5000, '콜라':2000}
print(dic1)
print(dic2)
print(dic3)
print(dic4)
print(dic5)
print(dic6)
print(dic7)
print(dic8)

A = set([6, 2023, 2, 1, 3, 5, 10, 100, 283])
B = set([3, 4, 6, 22, 100, 302, 2022])

print(A&B)
print(A|B)
print(A-B)
print(B-A)

def print_command():
    print('''1. icecream added
2. icecream price
3. icecream erase
4. icecream print
5. stop''')

def print_product(product):
    print('*'*50)
    for key in product.keys():
      print('{} : {}'.format(key, product[key] ))
    print('*'*50)

product = {'메로나': 1000,
       '비비빅': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

while True:
  print_command()
  command = input('pick what you want to do. ')
  if command == '1':
      ice_cream = input('add icecream : ')
      price = input('price : ')
      product[price]
  elif command == '2':
      ice_cream = input('change icecream : ')
      price = input('price : ')
      product[ice_cream:price]
  elif command == '3':
      ice_cream = input(' take out : ')
      del product[ice_cream]
  elif command == '4':
      print_product(product)
  elif command == '5':
      break
