import random
def attack(attacker, defender):
    damage = random.randint(1, attacker["attack"])

    if random.uniform(0,1) == 1:
        damage *= 2

    defender["hp"] -= damage

    print(attacker["name"], "hits", defender["name"], "for", damage)