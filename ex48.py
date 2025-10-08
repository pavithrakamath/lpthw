class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def enter(self):
        print(f"You have entered the {self.name}")

class Bedroom(Room):
    def __init__(self, name, description):
        super().__init__(name, description)

    def enter(self):
        print(f"Do not enter the {self.name}")

class Bathroom(Room):
    def __init__(self, name, description):
        super().__init__(name, description)
    
    def enter(self):
        print("Before entering the bathroom")
        super().enter()
        print("After entering the bathroom")

class Kitchen(Room):
    def __init__(self, name, description):
        # You think this will override the name of the room, but it doesn't
        # The name is still the same as the one passed in because the super().__init__() is called later with the original name
        self.name = f"{name} is in the kitchen"
        super().__init__(name, description)
    
if __name__ == "__main__":
    bedroom:Room = Bedroom("Bedroom", "A bedroom with a bed and a dresser")
    bathroom:Room = Bathroom("Bathroom", "A bathroom with a toilet and a sink")
    room:Room = bedroom
    room.enter()
    bathroom.enter()
    kitchen:Room = Kitchen("Kitchen", "A kitchen with a fridge and a stove")
    kitchen.enter()

    # Use dis to see the bytecode
    import dis
    print("*"*100)
    dis.dis(bedroom.enter)
    print("*"*100)
    dis.dis(bathroom.enter)
    print("*"*100)
    dis.dis(kitchen.enter)
    print("*"*100)