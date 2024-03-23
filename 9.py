tower1, tower2, tower3 = map(int, input().split())

if tower1 >= tower2 and tower1 >= tower3:
    max_height = tower1
    if tower2 >= tower3:
        mid_height = tower2
        min_height = tower3
    else:
        mid_height = tower3
        min_height = tower2
elif tower2 >= tower1 and tower2 >= tower3:
    max_height = tower2
    if tower1 >= tower3:
        mid_height = tower1
        min_height = tower3
    else:
        mid_height = tower3
        min_height = tower1
else:
    max_height = tower3
    if tower1 >= tower2:
        mid_height = tower1
        min_height = tower2
    else:
        mid_height = tower2
        min_height = tower1

print(max_height, mid_height, min_height)