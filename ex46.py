class Human(object):
    def __init__(self, name, age, gender):
      self.name = name
      self.age = age
      self.gender = gender

    def talk(self, words):
      print(f"{self.name} says {words}")

    def walk(self):
      print(f"{self.name} walks")

class Woman(Human):
    def __init__(self, name, age, gender):
      super().__init__(name, age, gender)
      self.gender = "female"

class Man(Human):
    def __init__(self, name, age, gender):
        # python2 style of calling parent's __init__() is to call Super with the class name and self
        # super(Man, self).__init__(name, age, gender)
        super().__init__(name, age, gender)
        self.gender = "male"
    def talk(self, words):
      print(f"{self.name} says {words} in a deep voice")

man = Man("John", 25, "male")
woman = Woman("Jane", 25, "female")
man.talk("Hello")
woman.talk("Hello")