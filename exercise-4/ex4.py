import re


class Passport:
    passport_fields = []
    mandatory_fields = [
        ['byr', 4, 1920, 2002],
        ['iyr', 4, 2010, 2020],
        ['eyr', 4, 2020, 2030],
        ['hgt', ['cm', 150, 193], ['in', 59, 76]],
        ['hcl', '#', 6, '[a-zA-Z0-9]'],
        ['ecl', ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']],
        ['pid', 9]]

    def __init__(self, passport_fields):
        self.passport_fields = passport_fields

    def contains_mandatory_fields(self):
        for mandatory_field in self.mandatory_fields:
            valid_found = False
            for field in self.passport_fields:
                if mandatory_field[0] in field:
                    valid_found = self.validate_field(mandatory_field, field)
            if not valid_found:
                return False
        return True

    @staticmethod
    def validate_field(mandatory_field, field: str):
        value = field.split(':')[1]
        if mandatory_field[0] == 'byr' or mandatory_field[0] == 'iyr' or mandatory_field[0] == 'eyr':
            return len(value) == mandatory_field[1] and mandatory_field[2] <= int(value) <= mandatory_field[3]
        elif mandatory_field[0] == 'hgt':
            if mandatory_field[1][0] in value:
                sanitized_value = int(value.replace(mandatory_field[1][0], ''))
                return mandatory_field[1][1] <= sanitized_value <= mandatory_field[1][2]
            elif mandatory_field[2][0] in value:
                sanitized_value = int(value.replace(mandatory_field[2][0], ''))
                return mandatory_field[2][1] <= sanitized_value <= mandatory_field[2][2]
        elif mandatory_field[0] == 'hcl':
            sanitized_value = value.replace(mandatory_field[1], '')
            return mandatory_field[1] in value and len(sanitized_value) == mandatory_field[2] and \
                   re.match(mandatory_field[3], sanitized_value)
        elif mandatory_field[0] == 'ecl':
            return value in mandatory_field[1]
        elif mandatory_field[0] == 'pid':
            return len(value) == mandatory_field[1]


class PassportGenerator:
    passport_list = []

    def generate_passports(self, entries):
        passport_entries = []
        for index, entry in enumerate(entries):
            if index == len(entries) - 1:
                [passport_entries.append(e) for e in entry.split(' ')]
                self.passport_list.append(Passport(passport_entries))
            elif entry:
                [passport_entries.append(e) for e in entry.split(' ')]
            elif not entry:
                self.passport_list.append(Passport(passport_entries))
                passport_entries = []
        return self.passport_list


class PassportValidator:
    validPassports = 0

    def validate_passports(self, passports):
        for passport in passports:
            if passport.contains_mandatory_fields():
                self.validPassports += 1
        print(self.validPassports)


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
    passports = PassportGenerator().generate_passports(file.get_file_entries())
    PassportValidator().validate_passports(passports)
