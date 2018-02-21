

class Parent(object):
    x = 5

class Child1(Parent):
    pass

class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)


Child2.x = 10
print(Parent.x, Child1.x, Child2.x)


Parent.x = 12
print(Parent.x, Child1.x, Child2.x)
