class Hands():
    fingers = 5

    def fingers_func(selfself):
        print('writing')

class Legs():
    fingers = 6

    def fingers_func(self):
        print('climbing')

class Human(Hands,Legs):

    def __init__(self):
        print(self.fingers)
        print(__class__)

Ram = Human()