class Point:
    # constructor
    def __init__(self, x, y):
        # add values from the generating to attributes in object
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# generate object
point1 = Point(10, 20)
# create an attribute
point1.z = 15

print(point1.z)

point1.draw()

point2 = Point()

