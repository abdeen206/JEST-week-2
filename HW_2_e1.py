#__author__ = Mohammad Abdin

class Human:
    human_conversation = []
    msg=''
    def __init__(self, name):
        self.name = name
        #print("human name is:{}".format(self.name))
    def send(self,msg):
        self.msg = msg
        self.human_conversation.append(msg)
        print(msg)


class Robot:
    robot_conversation = []
    msg =''
    def __init__(self, serial_number):
        self.serial_number = serial_number
        #print("robot serial number is:{}".format(self.serial_number))

    def send(self,msg):
        self.msg = msg
        self.robot_conversation.append(msg)
        print(msg)


class Chat:

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

    # def show_human_dialogue(self.human):
    #     return "{} said: {}".format(human.name,input())
    #
    # def show_robot_dialogue(self):
    #     return "{} said: {}".format(robot.serial_number, input())

def main():
    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)

    karl.send("Hi robot")
    bot.send("hi human")
    chat.show_human_dialogue()
    chat.show_robot_dialogue()

if __name__ == "__main__":
    main()

