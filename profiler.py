from subprocess import Popen, PIPE, STDOUT
from time import time

start = time()
p = Popen(["python", "main.py"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
_output = p.communicate(input=b"""4 1000000
3 2 5 3
5 4 6 1
9 5 7 3
6 8 3 4""")[0]
end = time()

print(_output.decode())
print("Time Elipsed: %.20f" % (end - start))
