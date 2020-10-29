class mob:
    def __init__ (self,name,health =10, power=2):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def get_hit (self,power):
        self.health = self.health - power

    def attack(self,enemy):
        enemy.get_hit(self.attack_power)

class hero(mob):
    def yell(self):
        print
hero = hero("keyz")
print(hero.attack_power)
bad_guy = mob("baddy")
hero.attack(bad_guy)
print(bad_guy.health)
