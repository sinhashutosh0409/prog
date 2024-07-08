from csv import writer

class CSVLogger:

    def __init__(self,file_object):
        self.file_object = file_object



    def log(self,message):
        words = message.split()
        csv_writer = writer(self.file_object)
        csv_writer.writerow(words)

class Filtered(CSVLogger):

    def __init__(self, some_word,file_object):
        self.some_word = some_word
        super().__init__(file_object)


    def log(self,message):
        if self.some_word in message:
            super().log(message)

f = open("text002.csv", "w")

d = Filtered("error",f)

d.log("hello hii how are you hello there error")




