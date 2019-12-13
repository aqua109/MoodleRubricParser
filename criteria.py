import unicodedata


class Criteria:
    def __init__(self, text, value):
        self.text = text
        self.value = value

    def get_criteria(self):
        return {"text": unicodedata.normalize("NFKD", self.text), "value": unicodedata.normalize("NFKD", self.value)}
