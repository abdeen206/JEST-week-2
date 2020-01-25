#__author__ = Mohammad Abdin

class Text:

    my_text = ''
    my_font = 'Arial'
    text_versions= []

    def __init__(self):
        self.my_text = input("input your text here:\n")
        #self.text_versions.append(self.my_text)

    def write(self, text):
        self.my_text = self.my_text + ' ' + text
        #self.text_versions.append(self.my_text)

    def set_font(self,font_name):
        self.my_font = font_name
        self.my_text = ''.join('['+ self.my_font + '] ' + self.my_text + ' [' + self.my_font + ']\n')
        #self.text_versions.append(self.my_text)

    def get_version(self,number):
        return  self.text_versions[number]

    def show(self):
        print(self.my_text)

    def get_text(self):
        return self.my_text

    def save_text(self,text):
        self.text_versions.append(self.my_text)
# ##############################
class SavedText(Text):

    def __init__(self):
        pass
    # my_text_tobe_saved = Text()
    # my_saved_text= my_text_tobe_saved.my_text
    my_saved_text_version = 0


    def restore(self, text_ver):
        text_ver = int(input("which version you wanna restore ?\n"))
        return self.get_text().get_version(text_ver)


t = Text()
s = SavedText()

#print("original text is : " + t.my_text + "\n")
additional_text = input("enter the additional text: ")
t.write(additional_text)
print("updated text is : " + t.my_text + "\n")

s.save_text(t)
print("saved text is : " + str(s.get_text()) + "\n")

t.set_font('David')
s.save_text(t)
print(t.my_text)

check_version = int(input("enter the version you want to access: "))
print(t.get_version(check_version))

print("show text:\n")
t.show()





