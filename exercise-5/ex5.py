
class SeatChecker:

    available_index: int
    min: int
    max: int
    lower_half = 'F'
    upper_half = 'B'
    lower_half_column = 'L'
    upper_half_column = 'R'

    seat_values = []
    all_seat_values = []
    max_score: int

    def __init__(self):
        self.available_index = 127
        self.max = 127
        self.min = 0
        self.max_score = 0

    def calculate_row(self, entries):
        for entry in entries:
            started_columns = False
            for indicator in list(entry):
                if indicator == self.lower_half or indicator == self.upper_half:
                    self.update_available_rows(indicator)
                elif indicator == self.lower_half_column or indicator == self.upper_half_column:
                    if not started_columns:
                        self.seat_values.append(self.min)
                        self.restart_values_for_columns()
                        started_columns = True
                    self.update_available_rows(indicator)
            self.seat_values.append(self.min)
            self.calculate_if_seat_values_produce_higher_score()
            self.restart_values_for_rows()
        print(self.max_score)
        self.find_first_available_seat()

    def update_available_rows(self, row_indicator):
        if row_indicator == self.lower_half or row_indicator == self.lower_half_column:
            self.max -= int(self.available_index / 2)
            self.available_index = int(self.available_index / 2)
        elif row_indicator == self.upper_half or row_indicator == self.upper_half_column:
            self.min += int(self.available_index / 2) + 1
            self.available_index = int(self.available_index / 2)

    def calculate_if_seat_values_produce_higher_score(self):
        new_score = self.seat_values[0] * 8 + self.seat_values[1]
        self.all_seat_values.append(new_score)
        if new_score > self.max_score:
            self.max_score = new_score

    def find_first_available_seat(self):
        sorted_list = sorted(self.all_seat_values)
        value = sorted_list[0]
        for seat_value in sorted_list:
            if value != seat_value:
                print(value)
                break
            value += 1

    def restart_values_for_rows(self):
        self.min = 0
        self.max = 127
        self.available_index = 127
        self.seat_values = []

    def restart_values_for_columns(self):
        self.available_index = 7
        self.max = 7
        self.min = 0


class LoadFile:
    lines = []

    def read_file(self):
        file = open("plane_seats.txt", "r")
        for line in file:
            self.lines.append(line.strip())

    def get_file_entries(self):
        return self.lines


if __name__ == "__main__":
    file = LoadFile()
    file.read_file()
    SeatChecker().calculate_row(file.get_file_entries())
