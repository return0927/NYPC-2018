_size, _rotates = [int(x) for x in input().split(" ")[:2]]


class Rotater:
    def __init__(self, stack):
        self.stack = stack
        self.size = len(self.stack)

    def _sort(self):
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.stack[i][j] > self.stack[i][j+1]:
                    self.stack[i][j], self.stack[i][j+1] = self.stack[i][j+1], self.stack[i][j]

        return self.stack

    def _rotate(self):
        self.stack = [[row[i] for row in self.stack] for i in range(len(self.stack[0]))][::-1]
        return self.stack

    def rotate(self, count):
        for _ in range(count):
            self._sort()
            self._rotate()
            # print(_)
            # print("\n".join([" ".join([str(i) for i in row]) for row in r.stack]))

    def rotate2(self, count):
        if count > 6:
            count = (count - 2) % 4 + 2

        self.rotate(count)


stacks = []
for _ in range(_size):
    stacks.append(
        [int(x) for x in input().split(" ")[:_size]]
    )

r = Rotater(stacks)
r.rotate2(_rotates)

print(
    "\n".join([" ".join([str(i) for i in row]) for row in r.stack])
)
