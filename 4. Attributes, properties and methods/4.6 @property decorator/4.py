class Color:
    def __init__(self, hexcode: str):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, new_hexcode: str):
        self._hexcode = new_hexcode
        self.r = int(new_hexcode[:2], 16)
        self.g = int(new_hexcode[2:4], 16)
        self.b = int(new_hexcode[4:], 16)
