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
    # for determining the strongest army
    def __init__(self):
        print("welcome the battle")

    def fight(self,army1,army2):

        i =0
        j=0
        round_no =1
        while army1.army_soldiers[i].is_alive and army2.army_soldiers[j].is_alive:
            round_no += 1
            print("*********** round {} **************".format(round_no))
            if isinstance(army1.army_soldiers[i],Defender):
                if army2.army_soldiers[j].attack > army1.army_soldiers[i].defense:
                    army1.army_soldiers[i].health = army2.army_soldiers[j].attack - army1.army_soldiers[i].defense
                    print("army 2 attacked a defender in army 2")

            elif isinstance(army2.army_soldiers[j],Defender):
                if army1.army_soldiers[i].attack > army2.army_soldiers[j].defense:
                    army2.army_soldiers[j].health = army1.army_soldiers[i].attack - army2.army_soldiers[j].defense
                    print("army 1 attacked a defender in army 2")

            #ARMY 2 ATTACKS ARMY 1
        #    army1.army_soldiers[i].health -= army2.army_soldiers[j].attack
            #ARMY 1 ATTACKS ARMY 2
        #    army2.army_soldiers[j].health -= army1.army_soldiers[i].attack
            if army2.army_soldiers[j].health <= 0:
                if j == len(army2.army_soldiers)-1:
                    print("army 1 won")
                    return True
                else:
                    #army2.army_soldiers[j].is_alive = False
                    print("army 2 soldier number: {} has died".format(j+1))
                    j +=1
                    continue
                # print("warrior 1 won ")
                # return True
            elif army1.army_soldiers[i].health <= 0:
                if i == len(army1.army_soldiers)-1:
                    print("army 2 won")
                    return False
                else:
                    #army1.army_soldiers[i].is_alive = False
                    print("army 1 soldier number: {} has died".format(i+1))
                    i +=1
                    continue
                # print("warrior 2 won ")
                # return False
        i += 1


army1 = Army()
army2 = Army()
army1.add_units(Warrior(),2)
army2.add_units(Defender(),2)
bat = Battle()
bat.fight(army1,army2)

