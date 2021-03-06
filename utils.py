import csv
import os


def load_text_file(name, filepath):
    inputs = []

    path = get_file_path(name, filepath)

    with open(path) as file:
        for line in file:
            inputs.append(int(line))

    return inputs


def load_csv_file(filename, executingfilepath):
    path = get_file_path(filename, executingfilepath)

    results = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:  # each row is a list
            for num in row:
                results.append(int(num))

    return results


def get_file_path(filename, executingfilepath):
    dirname = os.path.dirname(executingfilepath)
    path = os.path.join(dirname, filename)

    return path
