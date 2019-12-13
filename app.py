import keyboard
import csv
from criterion import Criterion


def readRubric():
    with open("rubric.csv", encoding="utf-8-sig") as csvfile:
        rdr = csv.reader(csvfile, delimiter=",")
        rubric = []
        for row in rdr:
            rubric.append(row)
        return rubric[1:]


def main():
    csv = readRubric()
    rubric = []
    for r in range(0, len(csv), 3):
        criterion = Criterion()
        criterion.parse_criterion(csv[r])
        criterion.parse_criteria([""] + csv[r][1:], csv[r+2])
        rubric.append(criterion.get_criterion())
    print(rubric)


if __name__ == "__main__":
    main()
