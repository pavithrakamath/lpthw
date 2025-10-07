## Passing dictionary to a function

def talk(who, words):
    print(f"{who["name"]} says {words}")

def quack(who, words):
    print(f"{who["name"]} quacks {words}")

person1 = {"name": "Pavithra", "age": 25, "height": 170, "talk": talk}
person2 = {"name": "duck", "age": 5, "height": 7, "talk": quack}

person1["talk"](person1, "Hello")
person2["talk"](person2, "Hello")


## Closures

def outer_function(who):
    def inner_function(words):
        print(f"{who["name"]} says {words}")
    return inner_function

person1_speak = outer_function(person1)
person2_speak = outer_function(person2)
person1_speak("ola")
person2_speak("quack")

## person dictionary
def person_dictionary(name, age, height):
    person = {"name": name, "age": age, "height": height}
    def talk(words):
        print(f"{person["name"]} says {words}")
    person["talk"] = talk

    return person

person1 = person_dictionary("Pavithra", 25, 170)
person2 = person_dictionary("duck", 5, 7)
# type of person1 is dict
print(type(person1))
# When we now call person1["talk"]("oho"), it will print "Pavithra says oho"
person1["talk"]("oho")
person2["talk"]("qua qua")

## Class
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def talk(self, words):
        print(f"{self.name} says {words}")

person1 = Person("Pavithra", 25, 170)
person2 = Person("duck", 5, 7)
# type of person1 is Person
print(person1.__class__)
# When we now call person1.talk("oho class"), it will print "Pavithra says oho class"

person1.talk("oho class")
person2.talk("qua qua class")

print(person1.__dict__)
print(dir(person1))

print(getattr(person1, "name"))

print(person1.__class__.__dict__["talk"])