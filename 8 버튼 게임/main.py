red, blue = [int(x) for x in input().split(" ")]

before = [None, None]

while True:
    if blue == 0 and red != 1:
        print("IMPOSSIBLE")
        break

    if blue > red:
        blue -= red

    elif blue < red:
        red -= blue

    else:  # blue == red
        blue -= red

    if before == [red, blue]:
        break

    before = [red, blue]

    if red < 0 or blue < 0:
        break

    if red == 1 and blue == 0:
        print("POSSIBLE")
        break
