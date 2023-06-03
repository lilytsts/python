from cs50 import get_string

people = {
    "Carter": "+1-211212",# : -> ключ значение
    "David": "+1-213212"
}

name = get_string("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")
