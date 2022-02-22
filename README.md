## First_Text_Game

###Objective

This is my first D&D-style text adventure game. The idea is that you head into a 
dungeon and encounter creatures that you will either have to fight or flee from. 
The center of the dungeon is a 'treasure room' where you obtain a 
randomly-generated special item that you can then hold on to for future excursions
into the dungeon. The player then must make it back out of the dungeon alive if 
they want to keep the booty. Since the idea of the game is that entering the 
dungeon is a risk/reward tradeoff, the further you get into the dungeon the more 
powerful the monsters will be. Ideally a player will just make it out with a few 
health points left. The exciting part is to see if one can fight and flee at the 
right times, of course with a heavy dose of randomness thrown in. At some point 
it might make sense to retreat from the dungeon and try again, then of course 
getting out with your life will be the tricky part. Getting pushed back a step is 
the is designed to be a constant obstacle, in addition to the damage taken during 
battle. 

In the future I'd also like to incorporate puzzles to act as 'booby traps' but I 
haven't figured that out yet. 

###Implemetation

The battle system incorporates some randomness in the form of an evade metric 
that allows both players and creatures to sometimes evade attacks. The same 
evade metric is used when a player attempts to flee a creature. 


###Challenges

The first challenge I ran into was that within my main game while loop I was 
instantiating Creature objects each time the player advanced another step. I
soon realized that instead of creating a new object the program was just reusing
old creatures, ones that had already been killed. At the time I didn't understand
OOP concepts well enough to grasp why this was happening but now, 7 months later, 
I believe I do and I'll be tackling this issue soon. 

