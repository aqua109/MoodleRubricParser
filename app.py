import keyboard
import csv
import json
import textwrap
import pandas as pd
from tabulate import tabulate
from criterion import Criterion
from rubric import Rubric


def read_rubric(filename):
    with open(f"{filename}.csv", encoding="utf-8-sig") as csvfile:
        rdr = csv.reader(csvfile, delimiter=",")
        rubric = []
        for row in rdr:
            rubric.append(row)
        return rubric[1:]


def create_rubric(csv):
    rubric = Rubric()
    for r in range(0, len(csv), 3):
        criterion = Criterion()
        criterion.parse_criterion(csv[r])
        criterion.parse_criteria([""] + csv[r][1:], csv[r+2])
        rubric.add_row(json.dumps(criterion.get_criterion()))
    return rubric


def display_rubric(rubric):
    columns = ["Criterion"] + [f"Criteria_{x+1}" for x in range(rubric.dict["criteria_count"])]
    data = []
    for i in range(rubric.dict["criterion_count"]):
        row = list()
        wrapper = textwrap.TextWrapper(width=20)

        row.append(wrapper.fill(rubric.dict["rubric"][i]["criterion"]))
        for j in range(rubric.dict["criteria_count"]):
            criteria = rubric.dict["rubric"][i]["criteria"][j]
            row.append(f"{wrapper.fill(criteria['text'])}\n{criteria['value']}")
        data.append(row)
    df = pd.DataFrame(data, columns=columns)
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))


def enter_rubric(rubric):
    count = 1
    length = rubric.dict["criterion_count"]
    for criterion in rubric.dict["rubric"]:
        count += 1
        keyboard.write(criterion["criterion"])
        keyboard.press_and_release("tab")
        for criteria in criterion["criteria"]:
            keyboard.write(criteria["text"])
            keyboard.press_and_release("tab")
            keyboard.write(str(criteria["value"]))
            keyboard.press_and_release("tab")
            keyboard.press_and_release("tab")
        if count != length:
            keyboard.press_and_release("tab")
        for i in range(4):
            keyboard.press_and_release("tab")


def main():
    filename = input("Enter .csv filename: ").replace(".csv", "")
    try:
        csv = read_rubric(filename)
        try:
            rubric = create_rubric(csv)
            display_rubric(rubric)
            confirmation = input("Is this correct [y/n]: ")
            if confirmation == "y":
                print("Open the desired 'Define Rubric' moodle page")
                print(f"Create {rubric.dict['criterion_count']} blank criterions with {rubric.dict['criteria_count']} blank levels")
                ready = ""
                while ready != "ready":
                    ready = input("Type 'Ready' when you are ready for input: ").lower()
                print("Make sure your cursor is in the first criterion input")
                print("Press insert to begin rubric input")
                keyboard.wait("insert")
                enter_rubric(rubric)
                print("Rubric entered")
            else:
                print("Adjust the .csv file and try again")
        except IndexError:
            print("Failed to read .csv file, please ensure formatting is correct")
    except FileNotFoundError:
        print(f"File: {filename} not found, please try again")
        main()


if __name__ == "__main__":
    main()
