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

class Pikachu(Pokemon):
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
        
pikachu1 = Pikachu(500,'quick attack',100)
pikachu1.print_hp()

pikachu2 = Pikachu(389,'mega bolt', 5000)
pikachu2.print_hp()

class Butterful(Pokemon):
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
        
pikachu1 = Butterful(500,'venom',100)
pikachu1.print_hp()

pikachu2 = Butterful(310,'solar beam', 400)
pikachu2.print_hp()

class Eevee(Pokemon):
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
        
pikachu1 = Eevee(500,'quick attack',100)
pikachu1.print_hp()

pikachu2 = Eevee(389,'lastresort', 500)
pikachu2.print_hp()
