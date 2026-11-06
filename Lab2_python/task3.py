
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(7, 12)
v2 = Vector(3, 5)

print("Перший вектор:", str(v1))
print("Представлення вектора:", repr(v1))
print("Другий вектор:", v2)

print("Сума:", v1 + v2)
print("Різниця:", v1 - v2)
print("Вектори рівні:", v1 == v2)
print("Довжина першого вектора:", round(abs(v1), 2))
