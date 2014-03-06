class Tank(object):
    def __init__(self, name): #constructor. name must be passed and will be assigned to self.name

        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def __str__(self): #way to return strings
        if self.alive:
            return "%s (%i armor, %i shells)"%(self.name, self.armor, self.ammo)
        else:
            return "%s (DEAD)"%self.name

    def fire_at(self, enemy): #method to fire. checks if we have ammo or not

        if self.ammo >= 1 and self.name != enemy.name:
            self.ammo-= 1
            print (self.name, "fires on", enemy.name)
            enemy.hit()
        elif self.name == enemy.name:
            print("You can't shoot yourself!")
        else:
            print (self.name, "has no shells!")

    def hit(self): #method to low armor if object is hit. checks if armor is less or equal to 0 and (if true) calls explode

        self.armor-= 20
        print (self.name, "is hit!")
        if self.armor <= 0:
            self.explode()

    def explode(self): #explode method changes alive bool to false and print that a tank has exploded

        self.alive = False
        print (self.name, "explodes!")
