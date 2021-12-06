def read_inputs(filename):
    with open(filename) as fd:
        return [line.strip('\n') for line in fd.readlines()]


def build_list(inputs, index):
    return [input_[index] for input_ in inputs]


def as_binary(integer):
    return int(integer, 2)


class Equal(Exception):
    pass


def find_most_common(inputs, index):
    entries = build_list(inputs, index)
    one_count = entries.count('1')
    if len(entries) / 2 == one_count:
        raise Equal()

    if one_count >= len(entries) / 2:
        return '1'

    return '0'


def reverse_item(item):
    return str(int(item, 2) ^ 1)


def filter_inputs(inputs, position, value):
    return list(filter(lambda input_: input_[position] == value, inputs))


def energy_diagnostic(inputs):
    gamma = ''
    epsilon = ''
    for i in range(len(inputs[0])):
        most_common = find_most_common(inputs, i)
        gamma += most_common
        epsilon += reverse_item(most_common)

    return as_binary(gamma) * as_binary(epsilon)


def find_oxygen_rate(inputs):
    loop = 0
    while len(inputs) > 1:
        try:
            most_common = find_most_common(inputs, loop)
        except Equal:
            most_common = '1'

        inputs = filter_inputs(inputs, loop, most_common)
        loop += 1

    return as_binary(inputs[0])


def find_CO2_rate(inputs):
    loop = 0
    while len(inputs) > 1:
        try:
            most_common = find_most_common(inputs, loop)
        except Equal:
            least_common = '0'
        else:
            least_common = reverse_item(most_common)
        inputs = filter_inputs(inputs, loop, least_common)
        loop += 1

    return as_binary(inputs[0])


print(energy_diagnostic(read_inputs('inputs.txt')))
print(
    find_oxygen_rate(read_inputs('inputs.txt'))
    *
    find_CO2_rate(read_inputs('inputs.txt')),
)
