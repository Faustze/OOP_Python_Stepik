class TitledText(str):
    def __new__(cls, content: str, text_title: str):
        instance = super().__new__(cls, content)
        instance._title = text_title
        return instance

    def title(self):
        return self._title