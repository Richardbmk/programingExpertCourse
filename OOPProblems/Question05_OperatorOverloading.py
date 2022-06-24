class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, vector):
        return self.a == vector.a and self.b == vector.b

    def __repr__(self):
        return f"Vector({self.a}, {self.b})"

    def __add__(self, vector):
        new_a = self.a + vector.a
        new_b = self.b + vector.b

        return Vector(new_a, new_b)

    def __sub__(self, vector):
        new_a = self.a - vector.a
        new_b = self.b - vector.b
        return Vector(new_a, new_b)

    def __mul__(self, vector):
        return self.a * vector.a + self.b * vector.b

v1 = Vector(3, 4)
v2 = Vector(-4, 5)

print(v1 == v2)

print(v1 == Vector(3,4))

print(repr(v1))

v3 = v1 + v2

print(repr(v3))

v4 = v2 - v1

print(repr(v4))

v5 = v1 * v2

print(v5)

