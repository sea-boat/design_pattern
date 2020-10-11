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


def shape_factory(shape: str = 'circle'):
    shapes = {
        'rectangle': Rectangle,
        'triangle': Triangle,
        'circle': Circle
    }
    return shapes[shape]()


if __name__ == "__main__":
    shape = shape_factory()
    shape.draw()
    shape = shape_factory('rectangle')
    shape.draw()
    shape = shape_factory('triangle')
    shape.draw()
