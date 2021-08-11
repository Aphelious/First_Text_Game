
import random
import time
from Actors import *
from constants import *



#######################
### Basic Variables ###
#######################


wait = 0

def display(a,b = 1):
    '''This function is called whenever printing narrative text to the screen. It adds a sleep time at the end of each printed line
    The first argument taken is a string, the message to be printed. The second argument taken is an integer that will be
    multiplied by the value of the variable 'wait'. By default this multiplier value is set to one (ie. no effect).'''
    print(a)
    time.sleep(wait * b)

step = 0


###########################
### Difficulty settings ###
###########################


difficulty = 'easy'

difficulty_dict = {'easy':0.5, 'medium':0.35, 'hard':0.2}

def empty_space_or_not():
    global step
    x = random.random()
    if x < difficulty_dict[difficulty]:
        display('The path seems quiet here, but there is a dark chill in the air...')
        step += 1
        return True
    else: False


#############
### Intro ###
#############

player = Player((input('What is your name, adventurer?')).strip())
print(player)

map(display, intro_list)
#display('You notice 3 potential entrances to the tomb. There\'s a murky lake with what looks like a sunken staircase...', 1.3)
#display('You also noticed a false granite wall that seems like it could be pushed...')
#display('You also see an entrance to a cave behind a thick overgrowth of vines...')

# path = None
# while path != 'sunken staircase' or 'granite wall' or 'hidden cave':
#     path = input('Which route do you want to take ' + player_name + '? Sunken staircase, Granite wall, or Hidden Cave?')
#     path = path.lower()
#     if path == 'sunken staircase':
#         time.sleep(wait/2)
#         print('You have chose the Sunken staircase...yikes. I mean, good luck!')
#         break
#     elif path == 'granite wall':
#         time.sleep(wait/2)
#         print('You have chosen a most horrible death...I mean, the Granite wall. Good for you!')
#         break
#     elif path == 'hidden cave':
#         time.sleep(wait/2)
#         print('You have chosen the Hidden Cave. Nice knowing you!')
#         break
#     else:
#         print('You have not entered a valid command. Responses must be typed exactly as they are presented you fool. Choose again!')
# time.sleep(wait)
# display('You enter the tomb through the ' + path + ''' and it is dark, cold, and you immediately get the feeling like something is
# watching you. This place does not want you here...''', 2)
# display('''Every step you take further into the tomb comes with the risk that you will encounter danger in the form of a creatures
# lurking in the dank passageways or a trap set by the tomb\'s designer.''', 2)
# display('''You will have to fight or retreat from creatures. You will have to disarm traps. Game play will be explained later.''')

ready = None
while ready != 'yes':
    ready = input('''If you make it 15 steps into the tomb you reach the main chamber. Grab what you can then you have
    to make it out alive. Are you ready? Type 'yes' to take your first step.''')
    ready = ready.lower()
    if ready == 'yes':
        step += 1
        break
    else:
        print('You did not enter a valid command, you fool. Type \'yes\' to take your first step')


# creature_list = [Goblin(), Golem(), Kobold(), Undead_Lurker(), Cave_Troll(), Ice_Spider(), Basilisk(), Dark_Shadow(), Demilich()]

creature_list = ['Goblin', 'Golem', 'Kobold', 'Undead_Lurker', 'Cave_Troll', 'Ice_Spider', 'Basilisk', 'Dark_Shadow', 'Demilich']

abil_dict = {
    "Chilling Bite": "-10% to enemy's evade rate",
    "Paralyzing Bite": "(- 20% to enemy's evade rate)",
    "Dark Cloak": "(+ 10% to evade rate)",
    "Confounding Terror": "(- 10% to enemy's evade and attack)",
}

###############
###Game Play###
###############


def sel_creat():
    if step in range(0, 12):
        creature = random.choice(creature_list[0:4])
    elif step in range(12, 22):
        creature = random.choice(creature_list[0:7])
    else:
        creature = random.choice(creature_list)
    display(f'You take another step and encounter a {creature.name} hiding in the dark!')
    print(creature)
    return creature

def choice():
    choice = input("Would you like to fight or flee?")
    choice = choice.lower()
    if choice == "fight":
        print(f'{player.name} chose to fight!')
        return 'fight'
    elif choice == 'flee':
        print(f'{player.name} chose to flee...')
        return 'flee'
    else: return f'{self.name} You must choose to either fight or flee'


def battle(creature, player):
    '''This is the battle function of the game. Creatures attack first. An evasion event is triggered
    before all attacks and, depending on the result the randomly-generated attack, either hits or does not.'''
    global step
    cache = {'attack':0, 'damage':0, 'items':None, 'abilities':None}
    while creature.get_health() > 0 and player.get_health() > 0:
        if player.evasion == False:
            x = creature.get_attack()
            cache["damage"] += x
            player.set_health(player.get_health() - x)
            display(f'{creature.name} hit you for {x}!')
            display(f'{player.name} your health is now {player.get_health()}')
        else:
            x = creature.get_attack()
            display(f'{player.name} evaded the {creature.name}\'s attack of {x}!')
            display(f'{player.name} your health is {player.get_health()}')
        action = input("What do you want to do: attack or attempt to flee")
        if action.lower() == "attack" and creature.evasion == False:
            x = player.get_attack()
            cache["attack"] += x
            if creature.get_health() > x:
                y = creature.get_health() - x
                creature.set_health(y)
                display(f'You hit the {creature.name} for {x}!')
                display(f'The {creature.name}\'s health is now {creature.get_health()}')
            else: creature.set_health(0)
            # if creature.get_health() <= 0:
            #     if creature.drop() != []:
            #         z = creature.drop()
            #         cache["abilities"] = z
            #         player.set_abil(z)
            #     break
            display(f'Prepare yourself, the {creature.name} is attacking!')
        elif action.lower() == "attack" and creature.evasion == True :
            display(f'The {creature.name} evaded {player.name}\'s attack!')
            display(f'Prepare yourself, the {creature.name} is attacking!')
        elif action.lower() == "flee" and player.evasion == False:
            display(f'{player.name}\'s attempt to flee failed! Get ready {creature.name} is attacking again!')
        else:
            display(f'''{player.name} your attempt to flee was successful! But you do not advance,
            you go back to step {step-1}''')
            step -= 1
    if creature.get_health() <= 0:
        display(f'{player.name} you have defeated the {creature.name}!')
        display(f'''In this battle you took {cache.get("damage")} damage, dealt {cache.get("attack")} damage,
picked up {cache.get("items", "no items")}, gained {cache.get("abilities", "no abilities")}, and have {player.get_health()} health remaining.''')
        cache.clear()
        step += 1
    else:
        display(f'{player.name} you have been slain by the {creature.name} and you drop your {player.items}!')
        cache.clear()

creature = None
challenges = ["Creature"]

# #This is the main loop that the game play occurs in. It generates a random selection of either creature
# #or trap for each step taken and displays the relevant outputs to guide the player through the challenge process.

while step < 30:
    print(f'step = {step}')
    if empty_space_or_not() is True:
        pass
    else:
        challenge = random.choice(challenges)
        if challenge == "Creature":
            creature = sel_creat()

            if choice() == "fight":
                print(f'Ready your weapon {player.name}, the {creature.name} is attacking!')
                battle(creature, player)
                continue
            elif choice() == "flee" and player.evade == False:
                display(player.name + '\'s flee attempt failed, get ready to fight!',2)
                battle(creature, player)
                continue
            else:
                display(player.name + '\'s attempt to flee was successful! but you do not advance, you go back to step ' + str(step))
                continue


