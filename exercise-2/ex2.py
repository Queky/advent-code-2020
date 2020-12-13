from typing import List


class PasswordData:

    min: int
    max: int
    letter: str
    password: str

    def __init__(self, entry: str):
        entry_data = entry.split(' ')
        self.get_min_and_max(entry_data[0])
        self.get_character(entry_data[1])
        self.get_password(entry_data[2])

    def get_min_and_max(self, min_max_values: str):
        min_value = int(min_max_values.split('-')[0])
        max_value = int(min_max_values.split('-')[1])
        if min_value <= max_value:
            self.min = min_value
            self.max = max_value
        else:
            self.min = max_value
            self.max = min_value

    def get_character(self, character: str):
        self.letter = character[0]

    def get_password(self, password: str):
        self.password = password


class PasswordValidator:

    passwords: List[PasswordData] = []

    def validate_passwords(self, data: PasswordData):
        occurrences = data.password.count(data.letter)
        if data.max >= occurrences >= data.min:
            self.passwords.append(data)

    def validate_passwords_2(self, data: PasswordData):
        if (data.password[data.min - 1] == data.letter and data.password[data.max - 1] != data.letter) \
                or (data.password[data.min - 1] != data.letter and data.password[data.max - 1] == data.letter):
            self.passwords.append(data)

    def get_valid_passwords_count(self):
        return len(self.passwords)


class LoadFile:

    lines = []

    def read_file(self):
        file = open("entries.txt", "r")
        for line in file:
            self.lines.append(line.strip())

    def get_file_entries(self):
        return self.lines


if __name__ == "__main__":
    LoadFile().read_file()
    passwordValidator = PasswordValidator()
    for entry in LoadFile().get_file_entries():
        passwordValidator.validate_passwords_2(PasswordData(entry))
    print(passwordValidator.get_valid_passwords_count())
