import typing as T


def read_numbers(filename: str) -> T.List[int]:
    with open(filename) as fd:
        for line in fd.readlines():
            yield(int(line))


def build_triple_sum_list(measures: T.List[int]) -> T.List[int]:
    current_sum = [0, 0]
    result = []
    for current_measure in measures:
        current_sum = [
            current_sum[0] + current_measure,
            current_sum[1] + current_measure,
            current_measure,
        ]
        result.append(current_sum.pop(0))

    # ignore the two first iteration, not relevant
    return result[2:]


def count_increase(measures: T.List[int]) -> int:
    prev = None
    increase = 0
    for current_measure in measures:
        if prev is not None and current_measure > prev:
            increase += 1

        prev = current_measure

    return increase


print(count_increase(read_numbers('data.txt')))
print(count_increase(build_triple_sum_list(read_numbers('data.txt'))))
