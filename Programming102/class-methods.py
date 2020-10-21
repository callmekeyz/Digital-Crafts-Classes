class mob:
    def __init__ (self,name,health =10, power=2):
        self.name = name
        self.health = health
        self.power = power

    def get_hit (self,power):
        self.health = self.health - power
        print(f"I {self.name} was hit for {power} points and now have {self.health} health")

    def attack(self,enemy):
        enemy.get_hit(self.power)

bad_guys = mob("evilmcevil",10,3)

hero = mob("sir barksalot",30,10)
print(hero.health)

bad_guys.attack(hero)

hero.attack(bad_guys)
hero.attack(bad_guys)
hero.attack(bad_guys)

all_units = [hero,bad_guys]
i=0
while i < 10:
    for u in all_units:
        print(u.get_hit(5))
        i+=1