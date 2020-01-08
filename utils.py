import os


def loadfile(name, filepath):
    inputs = []

    dirname = os.path.dirname(filepath)
    path = os.path.join(dirname, name)

    with open(path) as file:
        for line in file:
            inputs.append(int(line))

    return inputs
