import re


class CaseHelper:
    @staticmethod
    def is_snake(string) -> bool:
        return bool(re.match(r'[a-z]+_?[a-z]+', string))

    @staticmethod
    def is_upper_camel(string) -> bool:
        return bool(re.match(r'[A-Z]+[a-z]+[A-Z]*[a-z]+', string))

    @staticmethod
    def to_snake(string):
        return re.sub(r'(?<!^)([A-Z])', r'_\1', string).lower()

    @staticmethod
    def to_upper_camel(string):
        return ''.join(word.capitalize() for word in string.split('_'))