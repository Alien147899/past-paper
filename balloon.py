class balloon:
    __health = 100
    def __init__(self, Colour, DefenceItem):

        self.__colour = Colour
        self.__defenceItem = DefenceItem

    def ChangeHealth(self, health):
        self.__health = health + self.__health

    def GetDefenceItem(self):
        return self.__defenceItem

    def CheckHealth(self):

        if self.__health == 0 or self.__health < 0:
            return True
        else:
            return False




def Defend(Balloon1):
    strength_opponent = int(input("enter your opponent's strength:"))
    Balloon1.ChangeHealth(- strength_opponent)
    print(Balloon1.GetDefenceItem())


    if Balloon1.CheckHealth() == True:
        print("no remaining health")
    else:
        print("has remaining health")
    return Balloon1
color_in = input("enter colour:")
item = input("enter item:")
Balloon1 = balloon(color_in, item)
Balloon1 = Defend(Balloon1)
















