# %%
# class <Class Name>(Super Classes)
# in python 3 class have object as its super class by default, so the example is redundant
class MyClass(object):
    # instance_count is a class attribute because it is not declared inside a method
    instance_count = 0
    # __init__ is called when creating a new instance
    def __init__(self, value):
        #self.__value is an instance atribute because it is declared in the self variable
        self.__value = value
        MyClass.instance_count += 1
        print("instance No {} created".format(MyClass.instance_count))
    def aMethod(self, value):
        self.__value *= value
    # __str__ is a special method, it is used when you need to parse the object into a string
    def __str__(self):
        return "A MyClass instance with value " + str(self.__value)
    # __del__ is called when the instance is destoried.
    def __del__(self):
        MyClass.instance_count -= 1

myInstance = MyClass(42)
myInstance.aMethod(24)
# the last line can be written as this:
MyClass.aMethod(myInstance, 52)
print(myInstance)
print(MyClass.instance_count)
del(myInstance)
print(MyClass.instance_count)
# %%
