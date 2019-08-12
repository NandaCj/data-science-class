class Human():
    hands = 2
    legs = 2

    def __init__(self, fingers, hands):
        self.fingers = fingers
        self.hands = hands

    def print(self):
        print("self.hands :", self.hands)
        print("self.legs :", self.legs)
        print("self.fingers :", self.fingers)

    def take_object(self):
        print(self.__dict__)

    def hand_fun(self):
        print("Hand is used for Writing ....", self.hands)

    @staticmethod # decorator # decorates the function with special meanings/functions
    def something(base, inc):
        print("This is a static method..., " , base+inc)
        return base + inc

    def salary_increment(self, func_obj, base, inc):
        func_obj(base, inc)

    @classmethod
    def access_class_values(cls,hand,leg):
        cls.hands = hand
        cls.legs = leg
        print(cls.hands, cls.legs)


Ram = Human(fingers=5, hands=2)
Ravi = Human(fingers=6, hands=1)

Ram.print()
Ravi.print()

Ram.hand_fun()
Ravi.hand_fun()

Human.take_object(Ravi)
Ravi.take_object()
Human.hand_fun(Ram)
Ram.hand_fun()


# Human.something()
# Ravi.something()
# Ram.something()

Ravi.salary_increment(Ravi.something, base=2000, inc=200)
# Aceesing class Attributes:
    # Class Variables
Human.access_class_values(2,2)
Ravi.access_class_values(3,3)
Ram.access_class_values(1,3)

# Human.access_class_values()
# def func(a, b, c):
#     pass
#
# func(10, 20)

