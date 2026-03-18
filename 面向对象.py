
class Dog:
    def __init__(self,petname,temp):
        self.name = petname
        self.temperature = temp
        pass
    def status(self):
        print("Dog name is", self.name)
        print("Dog temperature is", self.temperature)
        pass
    def setTemperature(self,temp):
        self.temperature = temp
        pass
    def bark(self):
        print("Woof!")
        pass
    pass

lassie = Dog("Lassie", 37)
lassie.status()
lassie.setTemperature(39)
lassie.status()