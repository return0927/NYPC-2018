_people, _meet = [int(x) for x in input().split(" ")]

influ = {1}
meets = [[] for _ in range(_meet)]

for _ in range(_meet):
    x, y, c = [int(x) for x in input().split(" ")]

    meets[c-1].append({x, y})

for meet in meets:
    _temp = influ
    for pair in meet:
        if pair & _temp:
            _temp |= pair

    influ |= _temp

print(" ".join([str(x) for x in influ]))
