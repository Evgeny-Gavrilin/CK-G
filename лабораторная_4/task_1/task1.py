# TODO решите задачу
import json


def task() -> float:
    filename = 'input.json'
    with open(filename) as f:
        jsdata = json.load(f)
        sumvalue = sum([item["score"] * item["weight"] for item in jsdata])
    return round(sumvalue, 3)


if __name__ == '__main__':
    print(task())
