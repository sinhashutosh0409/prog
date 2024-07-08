class TextFile:

    def __init__(self, file_object):
        self.file_object = file_object

    def log(self, message):
        self.file_object.write(message)
        self.file_object.write("\n")
        self.file_object.flush()



class Filtered(TextFile):
    def __init__(self,some_word,file_object):
        self.some_word = some_word
        super().__init__(file_object)


    def log(self,message):
        for line in message:
            if self.some_word in line:
                super().log(line)

f = open("text1.txt","w")
obj = TextFile(f)
obj.log("hello there how are you")


