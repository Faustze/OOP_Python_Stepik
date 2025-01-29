def make_dartboard(n):
    dartboard = [[0] * n for _ in range(n)]
    step = 1
    while step < n - step:
        for row in range(step, n - step):
            for column in range(step, n - step):
                dartboard[row][column] += 1
        step += 1
    return dartboard

dartboard = make_dartboard(int(input()))

for line in dartboard:
    print(*line)