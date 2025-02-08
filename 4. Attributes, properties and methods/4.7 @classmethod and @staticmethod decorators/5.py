class StrExtension:

    @staticmethod
    def remove_vowels(string: str) -> str:
        vowels = set("aeiouyAEIOUY")
        return ''.join(char for char in string if char not in vowels)

    @staticmethod
    def leave_alpha(string: str) -> str:
        return ''.join(filter(str.isalpha, string))

    @staticmethod
    def replace_all(string: str, chars: str, char: str) -> str:
        translation_table = str.maketrans(chars, char * len(chars))
        return string.translate(translation_table)