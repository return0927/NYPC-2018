_count = int(input())

x, y = [], []
for _ in range(_count):
    _x, _y = [int(x) for x in input().split(" ")]

    x.append(_x)
    y.append(_y)

print(sum(x)/_count, sum(y)/_count)
