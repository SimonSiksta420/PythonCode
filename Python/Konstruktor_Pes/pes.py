class Dog:
    def __init__(self, color, velocity, race, bark):
        self.color = color
        self.velocity = velocity
        self.race = race
        self.bark = bark
    
    def walk(self, time):
        distance = time * self.velocity
        return distance
    
    def do_bark(self):
        print(self.bark)
        
class K9(Dog):
    
    def __init__(self, color, velocity, bark, race, bodycount):
        super().__init__(color, velocity, bark, race )
        self.bodycount = bodycount
        
    def catch_thief(self):
        self.do_bark()
        self.bodycount += 1
        return self.bodycount

Tira = Dog("brown", 5, "Labrador", "woof")

Hank = K9("black", 10, "woof", "German Shepherd", 0)
    print(Hank.race)
    print(Hank.walk(5))
    print(Hank.do_bark())
    print