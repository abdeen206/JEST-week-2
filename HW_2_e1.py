#__author__ = Mohammad Abdin

conversation = []

class Human:

    msg=''
    def __init__(self, name):
        self.name = name
        #print("human name is:{}".format(self.name))
    def send(self,msg):
        self.msg = self.name +" said: "+ msg
        conversation.append(self.msg)
        #print(self.msg)


class Robot:

    msg =''
    def __init__(self, serial_number):
        self.serial_number = serial_number
        #print("robot serial number is:{}".format(self.serial_number))

    def send(self,msg):
        self.msg = self.serial_number + " said: " + msg
        conversation.append(self.msg)
       # print(self.msg)



class Chat:
    my_conv =[]
    human = Human('')
    robot= Robot('')

    def __init__(self):
        print("welcome to chat\n")

    def connect_human(self,human):
        self.human = human
        print( "Human : {} is connected to chat".format(self.human.name))

    def connect_robot(self,robot):
        self.robot = robot
        print( "Robot : {} is connected to chat".format(self.robot.serial_number))

    def show_human_dialogue(self):
        self.my_conv = conversation
        for msg in self.my_conv:
            print(str(msg))

    def show_robot_dialogue(self):
        self.my_conv = conversation
        for msg in self.my_conv:
            msg1 = msg.split(":", 1)[0]
            msg = msg.split(":", 1)[1]
            for char in msg:
                # print(char)
                if char in 'aeiouAEIOU':
                    msg = msg.replace(char, '0')

                else:
                    msg = msg.replace(char, '1')
            print(msg1 + ": " + msg)
def main():
    chat = Chat()
    karl = Human("my human")
    bot = Robot("my robot")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    print("\n")
    karl.send("Hi robot")
    bot.send("hi human")
    bot.send("bye human")
    karl.send("bye robot")

    chat.show_human_dialogue()
    print("\n")
    chat.show_robot_dialogue()

if __name__ == "__main__":
    main()

