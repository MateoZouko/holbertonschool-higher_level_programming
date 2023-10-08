#!/usr/bin/python3

"""
    Write a script that adds all
    arguments to a Python list
    and then save them to a file
"""

from sys import argv
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """Main Function"""

    file = "add_item.json"
    try:
        with open(file, "r") as f:
            if f.read() == "":
                save_json([], file)
    except Exception:
        save_json([], file)

    data = load_json(file)
    for i in range(1, len(argv)):
        data.append(argv[i])

    save_json(data, file)
