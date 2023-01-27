class calc:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def add(self):
        print("Сложение")
        return f"{self.x + self.y}"
    def sub(self):
        print("Вычитание")
        return f"{self.x - self.y}"
    def mul(self):
        print("Умножение")
        return f"{self.x * self.y}"
    def truediv(self):
        print("Деление")
        return f"{self.x // self.y}"
a = calc(100,5)
print(a.add())
print(a.mul())
print(a.sub())
print(a.truediv())