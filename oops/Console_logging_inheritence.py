class ConsoleLogger:

    def log(self,message):
        print(message)

class FilterConsole(ConsoleLogger):

    def __init__(self,some_word):
        self.some_word = some_word

    def log(self,message):
        if self.some_word in message:
            print(message)

d = FilterConsole("info")
d.log("helle i have got an error info")

