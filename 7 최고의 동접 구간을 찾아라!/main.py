from time import time
_time = [0 for _ in range(24 * 60)]

_count = int(input())


def parse_time(*args):
    _out = []
    for t in args:
        _h, _m = t.split(":")
        _out.append(int(_h) * 60 + int(_m))
    return _out


def make_two(t):
    t = str(t)
    return "0"*(2-len(t))+t


_data = [input() for _ in range(_count)]

__start = time()
for _ in range(_count):
    _start, _end = parse_time(*_data[_].split(" "))

    for t in range(_start, _end):
        _time[t] += 1

_max = max(_time)
_start = _time.index(_max)

for idx in range(_start, 24 * 60):
    if _time[idx] < _max:
        break

print("{}\n{:2}:{:2} {:2}:{:2}".format(
    _max, make_two(_start // 60), make_two(_start % 60), make_two((idx) // 60), make_two((idx) % 60)
))
__time = time()
print(_time)
print(__time - __start)