class FishGroup(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update({
            day: 0 for day in range(0, 9)
        })

    def finish_day(self):
        new_group = FishGroup()
        for key, value in self.items():
            if key == 0:
                continue
            else:
                new_group[key - 1] = self[key]

        new_group.produce(self[0])
        return new_group

    def produce(self, number):
        self[6] += number
        self[8] = number

    def __len__(self):
        return sum(value for value in self.values())


def get_inputs(filename):
    with open(filename) as fd:
        return [int(i) for i in fd.readline().strip('\n').split(',')]


def main():
    group = FishGroup()

    for counter in get_inputs('inputs.txt'):
        group[counter] += 1

    print(group)

    for i in range(256):
        group = group.finish_day()

    print(len(group))


main()
