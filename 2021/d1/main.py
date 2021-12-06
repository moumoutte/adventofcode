import typing as T


def read_input(filename):
    with open(filename) as fd:
        for line in fd.readlines():
            yield line


def detect_coordonate(inputs: T.List[str]):
    horizontal, depth = (0, 0)

    for _input in inputs:
        action, many = _input.split(' ')
        many = int(many)
        if action == 'forward':
            horizontal += many
        elif action == 'down':
            depth += many
        elif action == 'up':
            depth -= many

    return horizontal, depth


def detect_coordonate_with_aim(inputs: T.List[str]):
    horizontal = depth = aim = 0

    for _input in inputs:
        action, many = _input.split(' ')
        many = int(many)
        if action == 'forward':
            horizontal += many
            depth += aim * many
        elif action == 'down':
            aim += many
        elif action == 'up':
            aim -= many

    return horizontal, depth


x, y = detect_coordonate(read_input('inputs.txt'))
print(x*y)
x, y = detect_coordonate_with_aim(read_input('inputs.txt'))
print(x*y)
