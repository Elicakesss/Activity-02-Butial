import random

#stats
level = 90
attack = 205
defense = 188
power = 110

#modifier
targets = 1
weather = 1
badge = 1
crit = 1
rand = random.uniform(0.85, 1)
stab = 1.5
type = 0.5
burn = 1
other = 1
    
modifier = targets * weather * badge * crit * rand * stab * type
damage = ((((((2 * level / 5)+ 2) * power) * (attack / defense ))) / (50 + 2 ) * modifier)

print("A level 95 Feraligatr appeared!")
print ("Charizard use Fire Blast!")
print ('Damage: ', round(damage))