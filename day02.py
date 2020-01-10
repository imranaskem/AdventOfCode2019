import utils


def process_inputs(inputs):
    for i in range(0, len(inputs), 4):
        opcode = inputs[i]
        first = inputs[i+1]
        second = inputs[i+2]
        result = inputs[i+3]

        if opcode == 99:
            break

        if opcode == 1:
            inputs[result] = inputs[first] + inputs[second]

        if opcode == 2:
            inputs[result] = inputs[first] * inputs[second]

    return inputs[0]


inputs = utils.load_csv_file("inputs/day02.csv", __file__)

inputs[1] = 12
inputs[2] = 2

print(process_inputs(inputs))
