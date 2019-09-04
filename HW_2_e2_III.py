#__author__ = Mohammad Abdin

class Warrior:
    def __init__(self):
        self.max_health = 50
        self.health = self.max_health
        self.attack = 5
        self.is_alive = True

class Knight(Warrior):
    def __init__(self):
        self.attack = 7
        self.max_health = 50
        self.health = self.max_health
        self.is_alive = True

class Defender(Warrior):
    def __init__(self):
        self.attack = 3
        self.max_health = 60
        self.health = self.max_health
        self.is_alive = True
        self.defense = 2
class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_health = 50
        self.health = self.max_health
        self.attack = 1

class Vampire(Warrior):
    def __init__(self):
        self.attack = 4
        self.max_health = 40
        self.health = self.max_health
        self.is_alive = True
        self.vampirism = 0.5

class Lancer(Warrior):
    def __init__(self):
        self.attack = 6
        self.max_health = 50
        self.health = self.max_health
        self.is_alive = True
        self.lancerism = 0.5

class Healer:

    def __init__(self):
        self.health = 60
        self.attack = 0
        self.heal_power = 2
        self.max_health = 0

    def heal(self, harmed):
        if self.health < self.heal_power:
            print("healer can no longer heal harmed soldier\n")
        else:
            if harmed.health + self.heal_power > harmed.max_health:
                harmed.health = harmed.max_health
            else:
                harmed.health += self.heal_power





class Army(object):

    healer_exists = False

    def __init__(self):
        self.army_soldiers=[]


    def add_healer(self):
        self.healer = Healer()
        self.healer_exists = True

    #for adding the chosen amount of units to the Army
    def add_units(self, army_type, add_amount_to_army):
        for i in range(add_amount_to_army):
            self.army_soldiers.append(army_type)
        print("army soldiers created number is: {}".format(len(self.army_soldiers)))


class Battle:

    def __init__(self):
        print("\nwelcome the battle")

    def handle_health(self, attacker , victim, healer = None):


        if isinstance(attacker, Vampire):
            attacker.health *= 1 +attacker.vampirism

        if isinstance(attacker, Lancer):
            attacker.health -= attacker.attack * attacker.lancerism

        if isinstance(victim, Defender):
            if attacker.attack > victim.defense:
                victim.health = attacker.attack - victim.defense
        elif isinstance(victim, Vampire):
            #attacker.health *= 1.5
            victim.health -= attacker.attack

        elif isinstance(victim, Warrior):
            victim.health -= attacker.attack
        elif isinstance(victim, Knight):
            victim.health -= attacker.attack
        elif isinstance(victim, Rookie):
            victim.health -= attacker.attack
        elif isinstance(victim, Lancer):
            victim.health -= attacker.attack

        else:
            victim.health -= attacker.attack

        if healer is not None :
            healer.heal(victim)
            healer.health  -= attacker.attack * 0.5
            print("harmer soldier got support by a healer")


    # for determining the strongest army
    def fight(self,army1,army2):

        i =0
        j=0
        round_no =1

        while army1.army_soldiers[i].is_alive and army2.army_soldiers[j].is_alive :
            round_no += 1
            print("*********** round {} **************".format(round_no))

            healer = None
            if army2.healer_exists:
                healer = army2.healer

            self.handle_health(army1.army_soldiers[i], army2.army_soldiers[j], healer)

            healer = None
            if army1.healer_exists:
                healer = army1.healer
            self.handle_health(army2.army_soldiers[j], army1.army_soldiers[i], healer)



            #ARMY 2 ATTACKS ARMY 1
        #    army1.army_soldiers[i].health -= army2.army_soldiers[j].attack
            #ARMY 1 ATTACKS ARMY 2
        #    army2.army_soldiers[j].health -= army1.army_soldiers[i].attack
            if army2.army_soldiers[j].health <= 0:
                if j == len(army2.army_soldiers)-1:
                    print("last soldier in army 2 died -> army 1 won")
                    return True
                else:
                    #army2.army_soldiers[j].is_alive = False
                    print("army 2 soldier number: {} has died".format(j+1))
                    j +=1

                # print("warrior 1 won ")
                # return True
            elif army1.army_soldiers[i].health <= 0:
                if i == len(army1.army_soldiers)-1:
                    print("last soldier in army 1 died -> army 2 won")
                    return False
                else:
                    #army1.army_soldiers[i].is_alive = False
                    print("army 1 soldier number: {} has died".format(i+1))
                    i +=1

                # print("warrior 2 won ")
                # return False
            #i += 1

healer = Healer()
army_1 = Army()
army_2 = Army()
army_3 = Army()
army_4 = Army()
army_5 = Army()
army_6 = Army()
army_1.add_units(Warrior(),6)
army_2.add_units(Defender(),5)
army_3.add_units(Knight(),4)
army_4.add_units(Vampire(),5)
army_5.add_units(Lancer(),5)
army_6.add_units(Warrior(),5)

army_6.add_healer()

bat = Battle()
print("\nBattle 1\n")
bat.fight(army_1,army_2)

print("\n---------------------------------\n")

print("Battle 2\n")
bat.fight(army_2,army_1)

print("\n---------------------------------\n")

print("Battle 3\n")
bat.fight(army_3,army_1)

bat = Battle()
print("\nBattle 4\n")
bat.fight(army_1,army_4)

bat = Battle()
print("\nBattle 5\n")
bat.fight(army_1,army_5)

bat = Battle()
print("\nBattle 6\n")
bat.fight(army_6,army_1)