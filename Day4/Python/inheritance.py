#!/usr/bin/python

class Parent:
  
    def __init__(self):
        print('Parent constructor')

    def sayHello(self):
        print('Parent sayHello function')

class Child(Parent):
 
    def __init__(self):
        Parent.__init__(self)
        print('Child constructor')

    def sayHello(self):
        Parent.sayHello(self)
        print('Child sayHello function')

childObj = Child()
childObj.sayHello()
