


class LoadFile:
    lines = []

    def __init__(self):
        pass

    def read_file(self):
        file = open("passports.txt", "r")
        for line in file:
            self.lines.append(line.strip())

    def get_file_entries(self):
        return self.lines


if __name__ == "__main__":
    file = LoadFile()
    file.read_file()
