class SuperHero:
    people='people'

    def __init__(self, name,nickname, superpower, health_points, catchphrase):
        self.name=name
        self.nickname = nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase
    def nyc(self):
        return f"name: {self.name}"

    def sum(self):
        return f"health_points: {self.health_points * 2}"

    def lime(self):
        return f"nick: {self.nickname}, super: {self.superpower}, health: {self.health_points}"

    def len(self):
        return len(self.catchphrase)
hero = SuperHero("Zara","Sam","running fast",100,"Im the best")
print(hero.nyc())
print(hero.sum())
print(hero.lime())
print(hero.len())