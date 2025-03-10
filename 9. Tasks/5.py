import re


class DomainException(Exception):
    pass


class Domain:
    def __init__(self, *args, **kwargs):
        self.args = args

    def __str__(self):
        return ''.join(self.args)
    
    def from_url(self, url: str):
        if url.startswith('https://'):
            return self.__class__(url[8:])
        elif url.startswith('http://'):
            return self.__class__(url[7:])
        raise DomainException('Недопустимый домен, url или email')
    
    def from_email(self, email: str):
        if re.match(r'[a-zA-Z]+@', email):
            return self.__class__(email[email.find('@') + 1:])
        raise DomainException('Недопустимый домен, url или email')



domain1 = Domain('pygen.ru')
domain2 = Domain.from_url('https://pygen.ru')
domain3 = Domain.from_email('support@pygen.ru')

print(domain1)
print(domain2)
print(domain3)