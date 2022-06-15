# 3- Methods 

# Sample 01
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

# p1 = Person("Richard")
# p2 = Person("Tim")

# p1.say_hello()
# p2.say_hello()

# p1.set_age(21)
# print(p1.age)
# print(p1.get_age())



# Sample 01 --> Evolution01
class Person:
    def __init__(self, name):
        self.name = name
        self.age = None

    def say_hello(self):
        print(f"Hello, {self.name}")

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

# p1 = Person("Richard")
# p2 = Person("Tim")

# p1.set_age(24)
# print(p1.get_age())

# Sample 02
class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        self.locked = not self.locked

    def increment(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count += 1

    def decrement(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count -= 1

    def print_count(self):
        print(f"The current count is {self.count}")


# counter = Counter()

# counter.increment()
# counter.increment()
# counter.increment()
# counter.increment()
# counter.increment()
# counter.decrement()
# counter.print_count()

# counter.toggle_lock()
# counter.increment()


# Joining to list together:
# --> https://www.w3schools.com/python/gloss_python_join_lists.asp


# 4- Properties

# Sample code 01
class Person:
    def __init__(self, name):
        self.name = name
        self._salary = 0

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Hey, this is invalid!")
        self._salary = salary

    def get_salary(self):
        return round(self._salary)

    salary = property(get_salary, set_salary)

p = Person("Richard")
p.salary = 103.989845
print(p.salary)

# Sample code 02
class Person:
    def __init__(self, name):
        self.name = name
        self._salary = 0

    @property
    def salary(self):
        return round(self._salary)

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Hey, this is invalid!")
        self._salary = salary

# p = Person("Richard")
# p.salary = 103.989845
# print(p.salary)

# Sample code 03
class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise ValueError("Invalid!")
        self._second = second

# t = Time(54)
# t.second = 59
# print(t.second)


# 5- Class Methods And Attributes

# Sample code 01
class Instructor:
    instructors = []

    def __init__(self, name):
        self.name = name
        Instructor.instructors.append(self)


# tim = Instructor("Tim")
# clement = Instructor("Clement")

# print(f"There are {len(Instructor.instructors)} instructors")
# for instructor in Instructor.instructors:
#     print(f"{instructor.name} is an instructor!")


# Sample code 02


class Car:
    number_of_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.number_of_cars += 1

    @classmethod
    def update_number_of_cars(cls, cars):
        cls.number_of_cars = cars
        print("run")

# Car.number_of_cars += 2
# print(Car.number_of_cars)

# c1 = Car("Ford", "Edge")
# c2 = Car("Mazda", "3")

# Car.update_number_of_cars(10)

# print(c1.number_of_cars)
# print(c2.number_of_cars)
# print(Car.number_of_cars)



# Sample code 03
class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius

    @classmethod
    def get_area_and_perimeter(cls, radius):
        return cls.area(radius), cls.perimeter(radius)


# print(Circle.area(3))
# print(Circle.perimeter(3))
# print(Circle.get_area_and_perimeter(3))


# 6- Static Methods

# Sample code 00
# Welcome to our Python playground!

import math


class Geometry:
    @staticmethod
    def perimeter_of_square(side_length):
        return 4 * side_length

    @staticmethod
    def area_of_square(side_length):
        return side_length ** 2

    @staticmethod
    def perimeter_of_circle(radius):
        return 2 * math.pi * radius

    @staticmethod
    def area_of_circle(radius):
        return math.pi * (radius ** 2)


# print("Perimeter of square with side of length 7:", Geometry.perimeter_of_square(7))
# print("Area of square with side of length 7:", Geometry.area_of_square(7))

# print("Perimeter of circle with radius of length 3:", Geometry.perimeter_of_circle(3))
# print("Perimeter of circle with radius of length 3:", Geometry.area_of_circle(3))


# Sample code 01
class Student:
    # static attribute
    grade_bump = 2.0

    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades
    
    # Instance method
    def average(self):
        return sum(self.grades) / len(self.grades)

    @classmethod
    def average_from_grades_plus_bump(cls, grades):
        average = cls.average_from_grades(grades)
        return min(average + cls.grade_bump, 100)

    @staticmethod
    def average_from_grades(grades):
        return sum(grades) / len(grades)


s1 = Student("Rick", [80, 75, 65, 100])
s2 = Student("Max", [100, 90, 65, 60])

# average = s1.average_from_grades(s1.grades)
# average = s2.average_from_grades(s1.grades)
average = Student.average_from_grades(s1.grades)
print(average)

# 7- Inheritance

# Sample code 00
# Welcome to our Python playground!


class Animal:
    def __init__(self, species):
        self.species = species


class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def speak(self):
        print(f"{self.species} named {self.name}: Woof!")


class Cat(Animal):
    def __init__(self, age):
        super().__init__("Cat")
        self.age = age

    def speak(self):
        print(f"{self.age} year old {self.species}: Miao!")


animals = [Dog("Rex"), Cat(13), Dog("Rose")]
# for animal in animals:
#     animal.speak()

# Sample code 01

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.last_name}")

class Employee(Person):
    def say_hello(self):
        print("----------")
        # super().say_hello()
        print("----------")

# e = Employee("Ryan", "Thecoder")
# e = Person("Ryan", "Thecoder")
# e = Employee("Ryan", "Thecoder")
# e.say_hello()
# e.test()


# p = Person("Ryan", "Thecoder")
# p.say_hello()
# e = Employee("Ryan", "Thecoder")
# e.say_hello()

# Sample Code 02

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.last_name}")

class Employee(Person):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def say_hello(self):
        super().say_hello()
        print(f"My salary is {self.salary}")


# e = Employee("Ryan", "Thecoder", 100000)
# e.say_hello()

# Sample Code 03

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.last_name}")

class Employee(Person):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def say_hello(self):
        super().say_hello()
        print(f"My salary is {self.salary}")


class Manager(Employee):
    def __init__(self, first_name, last_name, salary,\
         department):
         super().__init__(first_name, last_name, salary)
         self.department = department


m = Manager("Ryan", "Thecoder", 100000, "Sports")
m.say_hello()

# Sample code 04

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.last_name}")

class Employee(Person):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def say_hello(self):
        super().say_hello()
        print(f"My salary is {self.salary}")


class Manager(Employee):
    def __init__(self, first_name, last_name, salary,\
         department):
         super().__init__(first_name, last_name, salary)
         self.department = department

class Owner(Person):
    def __init__(self, first_name, last_name, net_worth):
        super().__init__(first_name, last_name)
        self.net_worth = net_worth


o = Owner("Ryan", "Thecoder", 1000000000)
o.say_hello()

print(type(o))
print(isinstance(o, Person))

# m = Manager("Tim", "Programmer", 50000, "Sports")
# print(isinstance(m, Person))
# print(isinstance(m, Employee))
# print(isinstance(m, Manager))
# print(isinstance(m, Owner))


# MRO = Method Resolution Order
# Sample code 05
class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A, B):
    pass

c = C()

# Sample code 05
class A:
    # def __init__(self):
    #     print("A")
    pass

class B:
    def __init__(self):
        print("B")

class C(A, B):
    def __init__(self):
        super().__init__()

c = C()


# 8- Abstract Classes

# Sample code 00

class AbstractVehicle:
    def get_max_speed(self):
        raise NotImplementedError

    def get_make(self):
        raise NotImplementedError

    def get_wheel_count(self):
        raise NotImplementedError

    def display(self):
        print(f"Make = {self.get_make()}, Wheel Count = {self.get_wheel_count()}, Top Speed = {self.get_max_speed()}")


class Car(AbstractVehicle):
    def __init__(self, make):
        self.make = make

    def get_wheel_count(self):
        return 4

    def get_make(self):
        return self.make


class Motorcycle(AbstractVehicle):
    def __init__(self, make):
        self.make = make

    def get_wheel_count(self):
        return 2

    def get_make(self):
        return self.make


class Tesla(Car):
    def __init__(self, model):
        super().__init__("Tesla")
        self.model = model

    def get_max_speed(self):
        if self.model == "Plaid":
            return 250
        return 200


class Yamaha(Motorcycle):
    def __init__(self):
        super().__init__("Yamaha")

    def get_max_speed(self):
        return 150


vehicles = [Tesla("Plaid"), Yamaha(), Tesla("S")]
# for vehicle in vehicles:
#     vehicle.display()



# Sample Code 01
import random

class AbstractGame:
    def start(self):
        while True:
            start = input("Would you like to play? ")
            if start.lower() == "yes":
                break
        
        self.play()

    def end(self):
        print("The game has ended.")
        self.reset()

    def play(self):
        raise NotImplementedError("You must provide an implementation for play()")

    def reset(self):
        raise NotImplementedError("You must provide an implementation for reset()")


class RandomGuesser(AbstractGame):
    def __init__(self, rounds):
        self.rounds = rounds
        self.round = 0

    def reset(self):
        self.round = 0

    def play(self):
        while self.round < self.rounds:
            self.round += 1

            print(f"Welcome to round {self.round}. Let's begin!")
            random_num = random.randint(0,10)
            while True:
                guess = input("Enter a number between 1-10: ")
                if int(guess) == random_num:
                    print("You got it!")
                    break

        self.end()


# game = RandomGuesser(3)
# game.play()
# game.start()

# 9- Interfaces

# Sample Code 00
# Welcome to our Python playground!

import io


class TranslatorInterface:
    def translate(self, text):
        raise NotImplementedError

    def untranslate(self, text):
        raise NotImplementedError


class SpanishTranslator(TranslatorInterface):
    def translate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "hello":
                words[i] = "hola"
            elif word == "world":
                words[i] = "mundo"
        return " ".join(words)

    def untranslate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "hola":
                words[i] = "hello"
            elif word == "mundo":
                words[i] = "world"
        return " ".join(words)


class FrenchTranslator(TranslatorInterface):
    def translate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "hello":
                words[i] = "bonjour"
            elif word == "world":
                words[i] = "monde"
        return " ".join(words)

    def untranslate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "bonjour":
                words[i] = "hello"
            elif word == "monde":
                words[i] = "world"
        return " ".join(words)


TRANSLATORS = {
    "spanish": SpanishTranslator(),
    "french": FrenchTranslator(),
}

# In order to check that the translator works correctly, we first
# translate "hello world" into that language, and then re-translate
# the result. At the end, we should be getting "hello world" back.
def check_translator_accuracy(language):
    translator = TRANSLATORS[language]

    original_text = "hello world"
    translated = translator.translate(original_text)
    new_text = translator.untranslate(translated)

    if original_text != new_text:
        raise Exception(f"Translator {language} does not work correctly!")

    print(f"The {language} translator is correct!")


# check_translator_accuracy("spanish")
# check_translator_accuracy("french")

# Sample Code 01
