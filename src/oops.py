#class

class firstclass:
    def __init__(self,name):
        self.name = name
    def yourname(self):
        return  f'here is my name {self.name}'

#object
a= firstclass('karthik')
b=a.yourname()
print(b)

#Encapsulation
# Control access using public /private attributes
class master:
    def __init__(self):
        self.__amount= 20
    def actual_func(self, bonus):
        self.__amount+=bonus
        return self.__amount

a = master()
b= a.actual_func(5)
print(b)



#inheritence

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")


#Polymorphism

def animal_sound(animal):
    animal.speak()

animal_sound(Dog())  # Output: Dog barks




