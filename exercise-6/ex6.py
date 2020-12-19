
class Answer:

    answered_list = []
    numAnswers: int

    def __init__(self, group_entries):
        self.numAnswers = 0
        for entry in group_entries:
            self.answered_list.append(list(entry))

    def get_answer_number(self) -> int:
        for answer in self.answered_list:
            for single_answer in list(answer):
                for answer2 in self.answered_list:
                    if not answer == answer2 and single_answer in answer2:
                        self.numAnswers += 1
        return self.numAnswers


class AnswerCalculator:
    answer_list = []

    def generate_answers(self, entries) -> [Answer]:
        passport_entries = []
        for index, entry in enumerate(entries):
            if index == len(entries) - 1:
                [passport_entries.append(e) for e in entry.split(' ')]
                self.answer_list.append(Answer(passport_entries))
            elif entry:
                [passport_entries.append(e) for e in entry.split(' ')]
            elif not entry:
                self.answer_list.append(Answer(passport_entries))
                passport_entries = []
        return self.answer_list

    def get_total_answers(self):
        res = 0
        for answer in self.answer_list:
            res += answer.get_answer_number()
        return res


class LoadFile:
    lines = []

    def read_file(self):
        file = open("answers.txt", "r")
        for line in file:
            self.lines.append(line.strip())

    def get_file_entries(self):
        return self.lines


if __name__ == '__main__':
    file = LoadFile()
    file.read_file()
    answers = AnswerCalculator()
    answers.generate_answers(file.get_file_entries())
    print(answers.get_total_answers())
