"""
This is the journal module
"""
import os


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join(".", "jornals", name + ".jrl"))
    return filename


def load(name):

    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for line in fin.readlines():
                data.append(line.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("..... saving to: {}".format(filename))

    with open(filename, "w") as fout:
        for line in journal_data:
            fout.write(line + "\n")


def add_entry(text, journal_data):
    journal_data.append(text)
