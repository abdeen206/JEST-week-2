#__author__ = Mohammad Abdin


class Friend:

    def __init__(self, friend_name, invite=None):
        self.friend_name = friend_name
        if invite is None:
            self.invite = ""
        else:
            self.invite = invite
        print("friend {} created".format(friend_name))

    def show_invite(self):
        return self.invite

class Party:
    name = ' '
    my_friend = Friend(name)


    def __init__(self,place,observers = None):
        self.place = place
        if observers is None:
            self.observers = []
        else:
            self.observers = observers

        print("party place is {} ".format(place))

    def add_friend(self, my_friend):
        if my_friend not in self.observers:
            self.observers.append(my_friend)
        #print("{} is added to observers".format(my_friend))
        print(str(my_friend.friend_name))

    def del_friend(self, friend):
        #self.observers.remove(friend)
        for i, o in enumerate(self.observers):
            if o.attr == friend:
                del self.observers[i]
                break


    def send_invites(self,day, time):
        for friend in self.observers:
            friend.invite = "party on {} at {}".format(day,time)
            print("{} is invited to {}".format(friend.friend_name,friend.invite))



party = Party("Midnight Pub")
nick = Friend("Nick")
john = Friend("John")
lucy = Friend("Lucy")
chuck = Friend("Chuck")

party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)

party.send_invites("Friday","21:30")

print(nick.show_invite())
