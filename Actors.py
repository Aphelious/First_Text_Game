#Actors - all beings in the game are actors -both creatures and players

#Tiers of creatures with increasing difficulty are added as the number of steps taken advances such that:
#1-10 steps - Tier 1
#11-20 steps - Tier 2
#21-30 steps - Tier 3
#Format for the 'creat_dict' creatures dictionary: "Creature name": [Health Points, Attack Points Range, Evade value, Abilities]

import random

class Actor():
    '''Use this class for all beings in the game, including creatures and players. While creatures technically have setters
    for attributes such as 'items' that wont be used for them, only for players as they pick up items throughout the game.'''

    # Getters and setters for health attribute. These will be called during a battle to model receiving an attack:

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = new_health

    # Getters and setters for attack attribute. These are used during a battle to model inflicting an attack:

    def get_attack(self):
        return random.randrange(self.attack_low,self.attack_high)

    def set_attack(self, new_attack_low, new_attack_high):
        self.attack_low = new_attack_low
        self.attack_high = new_attack_high

    # Getters and setters for the evade attribute. These will be used to model the efficacy of a flee attempt as well as
    # to increase the evade attribute whenever an item in aquired that increases the evade value :


    def get_evade(self):
        return float(self.evade)

    def set_evade(self, new_evade):
        self.evade = new_evade

    # Getters and setters for abilities attribute:

    @property
    def get_abil(self):
        if self.abil == []:
            return 'no abilities'
        else:
            return self.abil

    def set_abil(self, new_abil):
        self.abil = self.abil.append(new_abil)

    # Getters and setters for items attribute:

    @property
    def get_items(self):
        if self.items == []:
            return 'no abilities'
        else:
            return self.items

    def set_items(self, new_item):
        self.items = self.items.append(new_item)


    #Evade function for battle

    @property
    def evasion(self):
        x = self.get_evade()
        rand = random.random()
        if rand > x:
            return False
        else:
            return True

    def drop(self):
        x = None
        if self.get_health() <= 0:
            x = self.get_abil
        return x

class Creature(Actor):
    def __str__(self):
        return (f'This {self.name}\'s health is {self.health}\n'
        + f'This {self.name}\'s attack range is {self.attack_low} - {self.attack_high}\n'
        + f'This {self.name}\'s evade is {self.evade * 100}%\n'
        + f'This {self.name} has {self.get_abil}')

class Player(Actor):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_low = 3
        self.attack_high = 6
        self.evade = 0.2
        self.abil = []

    def __str__(self):
        return (f'{self.name} your health is {self.health}\n'
        f'Your attack range is {self.attack_low} - {self.attack_high} \n'
        f'Your evade is {self.evade * 100}%\n'
        f'You have {self.get_abil}')

class Goblin(Creature):
    def __init__(self):
        self.name = "Goblin"
        self.health = 3
        self.attack_low = 0
        self.attack_high = 3
        self.evade = 0
        self.items = []
        self.abil = 'Test ability'

class Golem(Creature):
    def __init__(self):
        self.name = "Golem"
        self.health = 4
        self.attack_low = 2
        self.attack_high = 4
        self.evade = 0.1
        self.items = []
        self.abil = 'Test ability'

class Kobold(Creature):
    def __init__(self):
        self.name = "Kobold"
        self.health = 4
        self.attack_low = 1
        self.attack_high = 4
        self.evade = 0.1
        self.abil = 'Test ability'

class Undead_Lurker(Creature):
    def __init__(self):
        self.name = "Undead Lurker"
        self.health = 6
        self.attack_low = 3
        self.attack_high = 6
        self.evade = 0.1
        self.items = []
        self.abil = 'None'

class Cave_Troll(Creature):
    def __init__(self):
        self.name = "Cave Troll"
        self.health = 8
        self.attack_low = 4
        self.attack_high = 7
        self.evade = 0
        self.items = []
        self.abil = 'None'

class Ice_Spider(Creature):
    def __init__(self):
        self.name = "Ice Spider"
        self.health = 7
        self.attack_low = 3
        self.attack_high = 6
        self.evade = 0.4
        self.items = []
        self.abil = "Chilling Bite (- 10% to enemy's evade rate)"

class Dark_Shadow(Creature):
    def __init__(self):
        self.name = "Dark Shadow"
        self.health = 10
        self.attack_low = 5
        self.attack_high = 9
        self.evade = 0.5
        self.items = []
        self.abil = "Dark Cloak (+ 10% to evade rate)"

class Basilisk(Creature):
    def __init__(self):
        self.name = "Basilisk"
        self.health = 15
        self.attack_low = 7
        self.attack_high = 11
        self.evade = 0.4
        self.items = []
        self.abil = "Paralyzing Bite (- 20% to enemy's evade rate)"

class Demilich(Creature):
    def __init__(self):
        self.name = "Demilich"
        self.health = 20
        self.attack_low = 9
        self.attack_high = 13
        self.evade = 0.3
        self.items = []
        self.abil = "Confounding Terror (- 10% to enemy's evade and attack)"

# creat_dict = {
#     "Goblin": [3,range(0,3),0,None],
#     "Golem": [4,range(1,4),0.1,None],
#     "Kobold": [2,range(0,3),0.3,None],
#     "Undead Lurker": [6,range(3,6),0.1,None],
#     "Cave Troll": [8,range(4,7),0,None],
#     "Ice Spider": [7,range(3,6),0.4,"Chilling Bite (- 10% to enemy's evade rate)"],
#     "Basilisk": [15,range(7,11),0.4,"Paralyzing Bite (- 20% to enemy's evade rate)"],
#     "Dark Shadow": [10,range(5,9),0.5,"Dark Cloak (+ 10% to evade rate)"],
#     "Demilich": [20,range(9,13),0.3,"Confounding Terror (- 10% to enemy's evade and attack)"]
#     }