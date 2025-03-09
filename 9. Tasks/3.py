import string


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift
        self.en_low = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
        self.en_up = string.ascii_uppercase   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def _transform(self, letter, alphabet, shift):
        if letter in alphabet:
            index = (alphabet.find(letter) + shift) % len(alphabet)
            return alphabet[index]
        return letter
    
    def encode(self, text):
        result = []
        for letter in text:
            if letter in self.en_low:
                result.append(self._transform(letter, self.en_low, self.shift))
            elif letter in self.en_up:
                result.append(self._transform(letter, self.en_up, self.shift))
            else:
                result.append(letter)             
        return ''.join(result)
    
    def decode(self, text):
        result = []
        for letter in text:
            if letter in self.en_low:
                result.append(self._transform(letter, self.en_low, -self.shift))
            elif letter in self.en_up:
                result.append(self._transform(letter, self.en_up, -self.shift))
            else:
                result.append(letter)      
        return ''.join(result)