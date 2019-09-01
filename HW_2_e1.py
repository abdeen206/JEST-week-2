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


def show_human_dialogue():
    for msg in conversation:
        print(str(msg))

def show_robot_dialogue():
    for msg in conversation:
        msg1 = msg.split(":", 1)[0]
        msg = msg.split(":", 1)[1]
        for char in msg:
            #print(char)
            if char in 'aeiouAEIOU'   :
                msg = msg.replace(char,'0')

            else:
                msg = msg.replace(char, '1')
        print(msg1+": "+ msg)

    # for i in range(len(conversation)):
    #     for j in range(len(conversation[i])):
    #         if conversation[i][j] in 'aeiouAEIOU':
    #             conversation[i] = conversation[i].replace(conversation[i][j],'0')
    #         else:
    #             conversation[i] = conversation[i].replace(conversation[i][j],'1')
    #     print(conversation[i])

# def show_robot_dialogue():
#     for msg in conversation:
#         msg1 = msg.split("said: ", 1)[0]
#         msg2 = msg.split("said: ", 1)[1]
#         #print(msg2)
#         for char in msg2:
#             #print(char)
#             if char in 'aeiouAEIOU'   :
#                 msg = msg2.replace(char,'0')
#
#             else:
#                 msg = msg2.replace(char, '1')
#         print(msg)


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


def main():
    chat = Chat()
    karl = Human("my human")
    bot = Robot("my robot")
    chat.connect_human(karl)
    chat.connect_robot(bot)

    karl.send("Hi robot")
    bot.send("hi human")
    bot.send("fuck u")
    show_human_dialogue()
    show_robot_dialogue()

if __name__ == "__main__":
    main()

