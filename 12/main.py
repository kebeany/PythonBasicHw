result = (0)

def add(num):
    global result
    result+=num
    return result

print(add(3))
print(add(4))

class calculator:
    def __init__(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result
    
call = calculator()

print(call. add(3))
print(call.add(4))

class calculator:
    def __init__(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result
    
    def sub(self,num):
        self.result -=num
        return self.result
    
call1 = calculator()
call2 = calculator()

print(call1. add(3))
print(call2.add(3))

print(call1.add(4))
print(call2.add(4))

print(call1.sub(1))
print(call2.sub(1))

class Pikachu:
    def __init__(self, hp, attack, damage):
        self.name = 'pikachu'
        self.hp = hp
        self.attack= attack
        self.damage= damage
        
    def set_hp (self,hp):
        self.hp = hp
        return self.hp

    def set_attack (self,attack):
        self.attack = attack
        return self.attack

    def set_damage (self,damage):
        self.damage = damage
        return self.damage
    
    def print_hp(self):
        print('hp:', self.hp)


pikachu1 = Pikachu(500,'quick attack',100)
pikachu1.print_hp()

pikachu2 = Pikachu(389,'thunderbolt', 135)
pikachu2.print_hp()

a = 10
print(type(a))

b = "10"
print(type(b))

c = [10]
print(type (c))

def func(x):
    return x +1
print(type(func))

a = 0.1#float
b = '''learned alot of Python'''#literal
c = ['철수', ':', '영희']#list
d = '나이 : 12'#literal
e = ('banana', 'grape', 'apple', 'melon')#tuple
f = "100"#literal
g = 100.#float
h = {'김밥':3000, '떡볶이':5000, '콜라':2000}#dict
i = -100#number
j = {'key': 'value'}#dict
k = (2021, 2022, 2023)#tuple
l = {'1', '2', '3'}#set
m = '2023' + '03'#literal
n = 2023 + 3#number

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
a = person('jack', 13)
b = person('sam', 12)

print('{} is {} years old.'.format(a.get_name(), a.get_age()))
print('{} is {} years old.'.format(b.get_name(), b.get_age()))

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def __str__(self):
        sentence = ("{} is {} years old".format(self.name,self.age))
        return sentence
    
a = person('jack', 13)
b = person('sam', 12)

print(a)
print(b)


class eevee:
    def __init__(self):
        self.name = 'eevee'
        self.hp = "eevee hp 50000"
        self.attack='quick attack'
        self.damage= "1300 damage given"

    def get_hp (self,hp):
        self.hp = hp
        return self.hp

    def get_attack (self,attack):
        self.attack = attack
        return self.attack

    def get_damage (self,damage):
        self.damage = damage
        return self.damage
    
call1 = eevee()
call2 = eevee()
call3 = eevee()

print(call1.hp)
print(call2.attack)
print(call3.damage)

