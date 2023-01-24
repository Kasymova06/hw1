class SuperHero:
    people='people'
    def __init__(self,name,nickname,supername, health_points,catchphrase) -> None:
        self.name = name
        self.nickname = nickname
        self.supername = supername
        self.health_points = health_points
        self.catchphrase = catchphrase
    def info(self):
        return f"Name: {self.name}, Catchphrase: {self.catchphrase}"
    def healthpoints(self):
        return f"Имя: {self.name}, его здоровье {self.health_points * 2}"

    def str(self):
        return f"nick: {self.nickname}, super-power: {self.supername}, health: {self.health_points}, catchphrase: {self.catchphrase}"
    def len(self):
        return len(self.catchphrase)

    
hero = SuperHero("sam","lime", "wet",111,"lighter")

class NewSuper(SuperHero):
    def __init__(self, name, nickname, supername, health_points, catchphrase) -> None:
         super().__init__(name, nickname, supername, health_points, catchphrase)
         self.damage = False
         self.fly = False
    def kvodrat(self):
        self.fly = True
        return f"rвадрат: {self.health_points ** 2}, Fly: {self.fly}"
    def newmetod(self):
        return f"newdamage: {self.damage}, newfly: {self.fly}"
    def flyg(self):
        return f"catchphrase: {self.catchphrase}"
newsuper = NewSuper("zahro", "snake", "web",6,"fly in the True phrase")
print(newsuper.kvodrat())
print(newsuper.flyg())
print(newsuper.newmetod())
class Villain(SuperHero):
    people = "monstr"
    def gen_x(self):
        pass
    def crit(self,damage1,damage2):
        return f"uron: {damage1 ** damage2}"
villain = Villain("sema", "fromLatoNYC", "Lenon",111,"iron man")
print(villain.crit(8,10))