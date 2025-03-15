class Testpaper:
    def __init__(self, theme, answers, passing_percent):
        self.theme = theme
        self.right_answers = answers
        self.passing_percent = int(passing_percent[:-1])


class Student:
    def __init__(self):
        self._tests_taken = {}

    @property
    def tests_taken(self):
        return self._tests_taken if self._tests_taken else 'No tests taken'

    def take_test(self, test, answers):

        right_answers_count = sum(answer in test.right_answers for answer in answers)
        test_procent = round(100 * (right_answers_count / len(test.right_answers)))
        if test_procent >= test.passing_percent:
            self._tests_taken[test.theme] = f'Passed! ({test_procent}%)'
        else:
            self._tests_taken[test.theme] = f'Failed! ({test_procent}%)'