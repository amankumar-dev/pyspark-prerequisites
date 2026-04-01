# 1) What is a class?
class person:
    a=10,
    b='temp'
    
    def __init__(self,name):
        self.name=name
    
    def meth(self):
        print('i am meth 1 ',self.name)

p=person('aman')
p.meth()

# 2) What is inheritance?
class son(person):
    def temp(self):
        print('r u winning son?')

s=son(person)
s.temp()

# 3) What is encapsulation?
class bankac:
    def __init__(self,bal):
        self.bal=bal
    def deposit(self,money):
        self.bal += money
b=bankac(1000)
b.deposit(500)
print(b.bal)

# 4) What is polymorphism?
class a:
    def meth():
        print('temp')
class b(a):
    def meth():
        print('temps')
        
bb=b
bb.meth()

# 5) What is method overloading vs overriding?
# Method Overloading
class x:
    def temp(self,a,b):
        print('temp')
    def temp(self,a,b,c):
        print('temps')
# Method Overriding
class dad:
    def temp():
        pass
class beta(dad):
    def temp():
        pass

