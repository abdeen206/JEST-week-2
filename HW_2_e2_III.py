#__author__ = Mohammad Abdin

class Warrior:
    def __init__(self):

        self.health =50
        self.attack = 5
        self.is_alive = True

class Knight(Warrior):
    def __init__(self):
        self.attack = 7
        self.health = 50
        self.is_alive = True

class Defender(Warrior):
    def __init__(self):
        self.attack = 3
        self.health = 60
        self.is_alive = True
        self.defense = 2


class Army(object):

    def __init__(self):
        self.army_soldiers=[]


    #for adding the chosen amount of units to the Army
    def add_units(self, army_type, add_amount_to_army):
        for i in range(add_amount_to_army):
            self.army_soldiers.append(army_type)
        print("army soldiers created number is: {}".format(len(self.army_soldiers)))


class Battle:

    def __init__(self):
        print("\nwelcome the battle")



    # for determining the strongest army
    def fight(self,army1,army2):

        i =0
        j=0
        round_no =1

        while army1.army_soldiers[i].is_alive and army2.army_soldiers[j].is_alive :
            round_no += 1
            print("*********** round {} **************".format(round_no))


            army1.army_soldiers[i].health = army2.army_soldiers[j].attack - army1.army_soldiers[i].defense if \
                isinstance(army1.army_soldiers[i], Defender) and \
                army2.army_soldiers[j].attack > army1.army_soldiers[i].defense \
                else army1.army_soldiers[i].health - army2.army_soldiers[j].attack

            army2.army_soldiers[j].health = army1.army_soldiers[i].attack - army2.army_soldiers[j].defense if \
                isinstance(army2.army_soldiers[j], Defender) and \
                army1.army_soldiers[i].attack > army2.army_soldiers[j].defense \
                else army2.army_soldiers[j].health - army1.army_soldiers[i].attack

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


army_1 = Army()
army_2 = Army()
army_3 = Army()
army_1.add_units(Warrior(),6)
army_2.add_units(Defender(),5)
army_3.add_units(Knight(),4)

bat = Battle()
print("\nBattle 1\n")
bat.fight(army_1,army_2)

print("\n---------------------------------\n")

print("Battle 2\n")
bat.fight(army_2,army_1)

print("\n---------------------------------\n")

print("Battle 3\n")
bat.fight(army_3,army_1)

