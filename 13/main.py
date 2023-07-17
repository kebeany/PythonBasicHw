class Animal:
    def __init__(self,age):
        self.age= age
    
    def eat(self):
        print('moving')

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(age)
        self.name = name
        print(self.name)

    def bark(self):
        print('bark bark')

    def shake(self):
        print('tails shaking')

    def __str__(self):
        sentence = 'name:{}, age:{}'.format(self.name,self.age)
        return sentence
    
dog = Dog('jack',2)
print(dog)

dog2 = Dog('june',5)
print(dog2)

dog3 = Dog('emily',7)
print(dog3)

class Animal:
    def eat(self):
        print('eating')
    
    def move(self):
        print('moving')

class Dog(Animal):
    def eat(self):
        print(' dog eating')
    
    def move(self):
        print(' dog moving')

class Bird(Animal):
    def eat(self):
        print(' Bird eating')
    
    def move(self):
        print('Bird moving')

animal = Animal()
animal.eat()
animal.move()

dog = Dog()
dog.eat()
dog.move()

bird = Bird()
bird.eat()
bird.move()

class Human:
    def __init__(self,name):
        self.name= name
        print(self.name)

    def __init__(self,age):
        self.age=age
        print(self.age)

class Teacher:
    def name(self):
        print('Pete')

    def age(self):
        print(25)

class Student:
    def name(self):
        print('Sean')
    
    def age(self):
        print(12)
    
teacher = Teacher()
teacher.name()
teacher.age()

student = Student()
student.name()
student.age()

class Pokemon:
    def __init__(self,hp,attack,damage):
        self.name = self
        self.hp=hp
        self.attack=attack
        self.damage=damage

    def set_hp(self,hp):
        self.hp=hp
        return self.hp
    
    def set_attack(self,attack):
        self.attack=attack
        return self.attack
    
    def set_damage (self,damage):
        self.damage = damage
        return self.damage
    
    def print_hp(self):
        print('hp:', self.hp)

class Pikachu(Pokemon):
    def __str__(self):
        s= '[pickachu] hp: {} attack: {} damage: {}'.format(self.hp,self.attack,self.damage)
        return s        

pikachu1 = Pikachu(500,'quick attack',100)
pikachu1.print_hp()
print(pikachu1)

pikachu2 = Pikachu(389,'mega bolt', 5000)
pikachu2.print_hp()
print(pikachu2)

class Butterful(Pokemon):
    def __str__(self):
        d='[butterful] hp: {} attack: {} damage: {}'.format(self.hp,self.attack,self.damage)
        return d
        
butterful1 = Butterful(500,'venom',100)
butterful1.print_hp()
print(butterful1)

butterful2 = Butterful(310,'solar beam', 4000)
butterful2.print_hp()
print(butterful2)

class Eevee(Pokemon):
    def __str__(self):
        e = '[eevee] hp: {} attack: {} damage: {}'.format(self.hp,self.attack,self.damage)
        return e
Eevee1 = Eevee(500,'quick attack',100)
Eevee1.print_hp()
print(Eevee1)
Eevee2 = Eevee(389,'lastresort', 500)
Eevee2.print_hp()
print(Eevee2)
