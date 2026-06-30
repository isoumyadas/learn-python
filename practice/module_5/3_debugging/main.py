"""

Complete the take_magic_damage function. 
It should return the new health after calculating how much magic-type damage the player takes. Here is a description of the parameters:

health: The player's starting health
resist: The player's magic resistance. This reduces the damage they take by a static amount
amp: The attacker's magic amplification. This increases the damage they deal by a multiplier
spell_power: The base damage of the spell
First, calculate the total maximum damage to be inflicted by multiplying the spell_power by the amp. 
Then, subtract the resist from the total damage to get the actual damage dealt. Apply that damage to the player's health and return the new health.


"""


def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp
    print(f"The total damage is {total_damage}")
    damage = resist - total_damage
    print(f"The damage is {damage}")
    new_health = damage + health
    print(f"The new Health is {new_health}")
    return new_health
