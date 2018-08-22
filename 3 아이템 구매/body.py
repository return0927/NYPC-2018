a, b = [int(x) for x in input().split(" ")]
d, u = sorted([a, b])
target = int(input())

switched = a == u
# Switched
#   True: a == u, b == d
#   False: a == d, b == u


for n in range(1, target//a + 1):
    if (target - a*n) % b == 0:
        print("{} {}".format(n, (target-a*n) // b))
        exit()

if target % a == 0:
    print("{} {}".format( target // a, 0))
    exit()

if target % b == 0:
    print("{} {}".format(0, target // b))
    exit()
