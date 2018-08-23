_score_table = [1, 2, 3, 4, 5, 6, 8, 10]

cases = int(input())

_storage = []

for _ in range(cases):
    _game_type = input()

    _temp = []
    for __ in range(8):
        _team, _time = input().split(" ")
        _m, _time = _time.split(":")
        _s, _ms = _time.split(".")

        _m, _s, _ms = int(_m), int(_s), int(_ms)

        _time = _m * 60 + _s + _ms / 1000

        _temp.append({"team": _team, "time": _time})
    _temp.sort(key=lambda x: x['time'])
    _storage.append([_game_type, _temp])

for _type, _records in _storage:
    if _type == "item":
        print(_records[0]['team'])
        continue
    elif _type == "speed":
        _mt = _records[0]['time']
        _board = {"red": 0, "blue": 0}

        for n in range(8):
            _game = _records[n]
            _team, _time = _game['team'], _game['time']

            if _time - _mt > 10:
                _score = 0
            else:
                _score = _score_table[7 - n]

            # print(_team, _score)
            _board[_team] += _score

        # print(_board)
        if _board['red'] > _board['blue']:
            print("red")
        else:
            print("blue")
