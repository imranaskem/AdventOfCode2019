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


def find_specific_output():
    inputs = utils.load_csv_file("inputs/day02.csv", __file__)
    specific_output = 19690720
    output = 0
    final_noun = 0
    final_verb = 0

    for noun in range(0, 99):

        for verb in range(0, 99):
            instance_inputs = inputs[:]
            instance_inputs[1] = noun
            instance_inputs[2] = verb

            output = process_inputs(instance_inputs)

            if output == specific_output:
                final_verb = verb
                break

        if output == specific_output:
            final_noun = noun
            break

    return (100 * final_noun) + final_verb


print(find_specific_output())
