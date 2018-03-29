# object oriented representation of a coordinate
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    # object representation of coordinates
    print('object repr:')
    obj_coordinates = [Coordinate(1, 2), Coordinate(1, 3), Coordinate(1, 4)]
    for coord in obj_coordinates:
        output = 'x: {} y: {}'.format(coord.x, coord.y)
        print(output)

    # dictionary representation of coordinates
    print('dictionary repr:')
    dict_coordinates = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 4}]
    for coord in dict_coordinates:
        output = 'x: {} y: {}'.format(coord['x'], coord['y'])
        print(output)

    # tuple version of coordinates
    # assumes you know what the ordered position means (x, y) in this case
    print('tuple repr:')
    tuple_coordinates = [(1, 2), (1, 3), (1, 4)]
    for coord in tuple_coordinates:
        output = 'x: {} y: {}'.format(coord[0], coord[1])
        print(output)

    # list version of coordinates, similar to the tuple
    print('list repr:')
    list_coordinates = [[1, 2], [1, 3], [1, 4]]
    for coord in list_coordinates:
        output = 'x: {} y: {}'.format(coord[0], coord[1])
        print(output)

if __name__ == '__main__':
    main()
