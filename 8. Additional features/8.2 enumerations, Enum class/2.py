from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, country_code):
        seasons_translate = {
            'en': {
                self.WINTER: 'winter',
                self.SPRING: 'spring',
                self.SUMMER: 'summer',
                self.FALL: 'fall'
            },
            'ru': {
                self.WINTER: 'зима',
                self.SPRING: 'весна',
                self.SUMMER: 'лето',
                self.FALL: 'осень'
            },
        }
        return seasons_translate[country_code][self]
