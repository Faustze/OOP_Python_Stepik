class Strip:
    def __init__(self, chars: str):
        self.chars = chars

    def __call__(self, string):
        for s in string:
            if s not in self.chars:
                alpha_start_ind = string.find(s)
                break

        for s in string[::-1]:
            if s not in self.chars:
                alpha_finish_ind = string.rfind(s)
                break

        return string[alpha_start_ind:alpha_finish_ind+1]