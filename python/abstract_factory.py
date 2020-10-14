class Operation:
    def __init__(self, shape_factory=None):
        self.shape_factory = shape_factory

    def operate(self):
        shape = self.shape_factory()
        print(shape)
        shape.draw()


class Rectangle:
    def __init__(self):
        self.shape = 'rectangle'

    def draw(self):
        print('draw a ' + self.shape)


class Triangle:
    def __init__(self):
        self.shape = 'triangle'

    def draw(self):
        print('draw a ' + self.shape)


class Circle:
    def __init__(self):
        self.shape = 'circle'

    def draw(self):
        print('draw a ' + self.shape)


if __name__ == "__main__":
    operation = Operation(Rectangle)
    operation.operate()
    operation = Operation(Triangle)
    operation.operate()
    operation = Operation(Circle)
    operation.operate()
