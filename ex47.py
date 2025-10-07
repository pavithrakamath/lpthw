"""
The process of building a program
********************************
-> Write or draw about the problem
-> Extract key concepts from Step #1 and research them
-> Create a class hierarchy and object map for the concepts
-> Code the classes and a test to run them
-> Repeat and refine
********************************
"""

from random import randint

from ex47_dialogue import dialogue


class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        exit(1)
    
class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes.",
    ]
    def enter(self):
        print(self.quips[randint(0, len(self.quips) - 1)])
        exit(1)
    
class CentralCorridor(Scene):
    def enter(self):
        print(dialogue['CentralCorridor_enter'])
        action = input("> ")
        if action == 'shoot':
            print(dialogue['CentralCorridor_shoot'])
            return 'death'
        elif action == 'dodge':
            print(dialogue['CentralCorridor_dodge'])
            return 'death'
        elif action == 'tell a joke':
            print(dialogue['CentralCorridor_joke'])
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
        return 'laser_weapon_armory'
    
class LaserWeaponArmory(Scene):
    def enter(self):
        print(dialogue['LaserWeaponArmory_enter'])
        code="123"  #f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
        guess = input("[keypad]> ")
        guesses = 0
        while guesses < 3 and guess != code:
            print("BZZZZZZZZ")
            guesses += 1
            guess = input("[keypad]> ")
        if guess == code:
            print(dialogue['LaserWeaponArmory_guess'])
            return 'the_bridge'
        else:
            print(dialogue['LaserWeaponArmory_fail'])
            return 'death'
            
class TheBridge(Scene):
    def enter(self):
        print(dialogue['TheBridge_enter'])
        action = input("> ")
        if action == 'throw the bomb':
            print(dialogue['TheBridge_throw_bomb'])
            return 'death'
        elif action == 'place the bomb':
            print(dialogue['TheBridge_place_bomb'])
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'
    
class EscapePod(Scene):
    def enter(self):
        print(dialogue['EscapePod_enter'])

        good_pod = randint(1, 5)
        guess = input(f"[pod #]> ")
        if guess == good_pod:
            print(dialogue['EscapePod_escape'])
            return 'finished'
        else:
            print(dialogue['EscapePod_death'].format(guess=guess))
            return 'death'

    
class Finished(Scene):
    def enter(self):
        print("You won!")
        return 'finished'
    
class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'finished': Finished(),
        'death': Death(),
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


if __name__ == "__main__":
    a_map = Map('central_corridor')
    a_game = Engine(a_map)
    a_game.play()