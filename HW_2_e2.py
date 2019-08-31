#__author__ = Mohammad Abdin

class Warrior:
    health =50
    attack = 5

    is_alive = True

class Knight(Warrior):
    attack = 7


def fight(w1,w2):
    while w1.is_alive and w2.is_alive:
        w2.health -= w1.attack
        w1.health -= w2.attack
        if w2.health <= 0:
            w2.is_alive = False
            print("warrior 1 won ")
            return True
        elif w1.health <= 0:
            w1.is_alive = False
            print("warrior 2 won ")
            return False

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()

fight(chuck, bruce) == True
fight(dave, carl) == False
# chuck.is_alive == True
# bruce.is_alive == False
# carl.is_alive == True
# dave.is_alive == False
