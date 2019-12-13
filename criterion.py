import json
import unicodedata
from criteria import Criteria


class Criterion:
    def __init__(self):
        self.criterion = ""
        self.criteria = []

    def parse_criterion(self, criterion):
        self.criterion = unicodedata.normalize("NFKD", criterion[0])

    def parse_criteria(self, criteria, values):
        criteria, values = criteria[1:], values[1:]
        for i in range(len(criteria)):
            self.criteria.append(Criteria(criteria[i], values[i]).get_criteria())

    def get_criterion(self):
        return {"criterion": self.criterion, "criteria": self.criteria}
