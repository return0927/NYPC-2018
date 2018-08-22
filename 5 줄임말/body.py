import os
os.chdir("C:/users/bjleh/downloads")

_temp = input()

lines = open(_temp, "r", encoding='UTF-8').readlines()

_out = []
for line in lines:
    _out.append("".join([x[0] for x in line.split(" ")]))

open(f"out-{_temp}", "w", encoding="UTF-8").write("\n".join(_out))
