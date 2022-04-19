print("hi")
class person:
    name = ""
    money = 0
    age = 0

    def getname():
        return name
    def getmoney():
        return money
    def getage():
        return age
    def setname(self):
        name = self
    def setmoney(self):
        money = self
    def setage(self):
        age = self

    def steal_money(self):
        if (money-self >= 0):
            money -= self
        else:
            print("You are to broke to steal from. Go away!")

    def give_money(self):
            print("Take the dough!")
            money += self