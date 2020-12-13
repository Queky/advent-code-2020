
class Passport:

    passport_fields = []
    mandatory_values = [
        ['byr', 4, 1920, 2002],
        ['iyr', 4, 2010, 2020],
        ['eyr', 4, 2020, 2030],
        ['hgt', ['cm', 150, 193], ['in', 59, 76]],
        ['hcl', '#', '[a-zA-Z0-9]'],
        ['ecl', ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']],
        ['pid', 9]]

    def __init__(self, passport_fields):
        self.passport_fields = passport_fields

    def contains_mandatory_fields(self):
        for mandatory_value in self.mandatory_values:
            any_found = False
            for field in self.passport_fields:
                if mandatory_value[0] in field:
                    any_found = True
            if not any_found:
                return False
        return True

    def validate_field(self, field):
        pass


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