from subprocess import Popen, PIPE, STDOUT
from time import time

_comm = 'python "11 전염병 역학 조사/main.py"'

start = time()
p = Popen(_comm, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
_output = p.communicate(input=b"""7 10
5 6 2
2 3 1
1 3 3
4 5 1
4 5 3
4 2 6
3 2 5
3 5 6
5 1 5
4 6 5""")[0]
end = time()

print(_output.decode())
print("Time Elipsed: %.20f" % (end - start))
