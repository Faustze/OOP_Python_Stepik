import re


class DomainException(Exception):
    pass


class Domain:
    __CORRECT_DOMAIN = r'\w+\.\w+'
    __CORRECT_URL = fr'^https?://(?P<domain>{__CORRECT_DOMAIN})$'
    __CORRECT_EMAIL = fr'\w+@(?P<domain>{__CORRECT_DOMAIN})'

    def __init__(self, domain):
        if not re.fullmatch(self.__CORRECT_DOMAIN, domain):
            raise DomainException('Недопустимый домен, url или email')
        self.domain = domain

    def __str__(self):
        return self.domain
    
    @classmethod
    def from_url(cls, url: str):
        url = re.match(cls.__CORRECT_URL, url)
        if not url:
            raise DomainException('Недопустимый домен, url или email')
        return cls(url.group('domain'))
    
    @classmethod
    def from_email(cls, email: str):
        email = re.match(cls.__CORRECT_EMAIL, email)
        if not email:
            raise DomainException('Недопустимый домен, url или email')
        return cls(email.group('domain'))