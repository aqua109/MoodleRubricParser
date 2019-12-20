import json


class Rubric:
    def __init__(self):
        self.dict = {"criterion_count": 0, "criteria_count": 0, "rubric": []}

    def add_row(self, json_str):
        j = json.loads(json_str)

        self.dict["criterion_count"] += 1
        self.dict["criteria_count"] = len(j["criteria"])
        self.dict["rubric"].append(j)

    def __str__(self):
        return str(json.dumps(self.dict))

    def get_dict(self):
        return self.dict
