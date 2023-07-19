try:

    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print('you cant divide by 0')
except IndexError:
    print('can not be indexed')

try:

    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:

    a = [1,2]
    print(a[3])

    4/0
except (ZeroDivisionError,IndexError)as e:
    print(e)

try:
    f= open("I don't have.txt",'r')
except FileNotFoundError:
    pass

try:
    x = 10/5
except:
    print("A exceotion occured")
else:
    print("no exception")

try:
    f= open("foo.txt",'w')
except:
    print("A exceotion occured")
else:
    print("no exception")


finally:
    f.close()

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle=Eagle()
eagle.fly()

class Eagle(Bird):
    def fly(self):
        print("veryfast")

eagle= Eagle()
eagle.fly()

class MyException(Exception):
    pass

def say_nick(nick):
    if nick =='stupid':
        raise MyException()
    print(nick)

say_nick('smart')
say_nick('stupid')

try:
    say_nick('smart')
    say_nick('stupid')
except MyException:
    print('you shouldn\'t give that type of nickename')

try:
    say_nick("smart")
    say_nick("stupid")
except MyException as e:
    print(e)

class MyException(Exception):
    def __str__(self):
        return""
try:
    say_nick("smart")
    say_nick("stupid")
except MyException as e:
    print(e)

string = input('num:')

number = int(string)

print(number + 10)

try:
    x = 100 / 5
except:
    print("there is an error.")
else:
    print("it finished normally.")

def scope():
    global var1
    var1 = 'usefulness of global codes'
    var2 = 'local variable'
    print('inside then function var1: ', var1)
    print('inside the function var2: ', var2)
    
var1 = 'global variable1'
var2 = 'global variable2'
 
print('before function var1: ', var1)
print('before function var2: ', var2)
     
scope()

print('after function var1: ', var1)
print('after function var2: ', var2)

var = 'global variable'

print(var, ' [ scope() output before exicution]')
 
def scope():
    var = 'local variable'
    print(var, ' [ scope() output from function ]')

    if True:
        print(var, ' [ if output from statement ]')

    for i in range(3):
        var = 'for local variiable'
        print(var, ' [ for output from statement]')   
 
scope()

print(var, ' [ scope() output from outside function]')
