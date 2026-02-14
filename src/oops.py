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
print(f'encrypted :{b}')



#inheritence

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meow")

a= Animal()

#Polymorphism

def animal_sound(animal):
    animal.speak()

animal_sound(Animal())

#Polymorphism best example

class Payment:
    def pay(self, amount):
        print("Processing payment...")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


def process_payment(payment_method, amount):
    payment_method.pay(amount)

process_payment(CreditCard(), 100)
process_payment(PayPal(), 200)
process_payment(UPI(), 50)





