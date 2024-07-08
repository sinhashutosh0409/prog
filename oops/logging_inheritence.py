from csv import writer

class ConsoleLogger:
    def log(self,message):
        print(message)

class TextFileLogger:

    def __init__(self,file_object):
        self.file_object = file_object

    def log(self,message):
        self.file_object.write(message)
        self.file_object.write("\n")
        self.file_object.flush()


class CSVFileLogger:

    def __init__(self,file_object):
        self.file_object = file_object

    def log(self,message):
        words = message.split()
        csv_writer = writer(self.file_object)
        csv_writer.writerow(words)
        self.file_object.flush()

class Filtered_Console(ConsoleLogger):

    def __init__(self,some_word):
        self.some_word = some_word

    def log(self,message):
        if self.some_word in message:
            super().log(message)

class Filtered_text(TextFileLogger):
    def __init__(self,some_word, file_object):
        self.some_word = some_word
        super().__init__(file_object)

    def log(self,message):
        if self.some_word in message:
            super().log(message)

class Filtered_csv(CSVFileLogger):
    def __init__(self,some_word, file_object):
        self.some_word = some_word
        super().__init__(file_object)


    def log(self,message):
        if self.some_word in message:
            super().log(message)


# f = open("text001.txt","w")
# d = Filtered_text("hello", f)
# d.log("hell there how are you")

f = open("text002.csv", "w")
d=Filtered_csv("error", f)
d.log("hello there i have got an error")









