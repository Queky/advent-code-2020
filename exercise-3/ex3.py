
class Map:

    maxWidth = 0
    maxHeight = 0
    positions = []

    def __init__(self, lines):
        self.maxWidth = len(lines[0])
        self.maxHeight = len(lines)
        for line in lines:
            if line:
                self.positions.append(list(line))

    def is_tree(self, x, y):
        return self.positions[y][self.normalize_x(x)] == '#'

    def normalize_x(self, x):
        return x % self.maxWidth

    def is_end(self, y):
        return y >= self.maxHeight


class Player:

    encounteredTrees = 0
    posX = 0
    posY = 0
    map: Map

    def __init__(self, map):
        self.map = map

    def run(self):
        while not self.map.is_end(self.posY):
            self.check_if_player_found_tree(self.posX, self.posY)
            self.move_forward()
        print('Encountered trees -> ' + str(self.encounteredTrees))

    def check_if_player_found_tree(self, x, y):
        if self.map.is_tree(x, y):
            self.encounteredTrees += 1

    def move_forward(self):
        self.posX += 3
        self.posY += 1


class LoadFile:

    lines = []

    def __init__(self):
        pass

    def read_file(self):
        file = open("map.txt", "r")
        for line in file:
            self.lines.append(line.strip())

    def get_file_entries(self):
        return self.lines


if __name__ == "__main__":
    file = LoadFile()
    file.read_file()
    Player(Map(file.get_file_entries())).run()