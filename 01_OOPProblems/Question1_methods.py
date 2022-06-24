
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Write your code here
    def get_position(self):
        return self.x, self.y

    def change_position(self, x, y):
        self.x = x
        self.y = y
        return x,y

    def get_area(self):
        return self.width * self.height

rect = Rectangle(10, -5, 5, 3)

pos = rect.get_position()
print(pos)

rect.change_position(3, 4)
pos = rect.get_position()
print(pos)

area = rect.get_area()
print(area)


