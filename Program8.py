# Matrix Path Optimizer using Dynamic Programming

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix values:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

dp = [[0] * cols for _ in range(rows)]

dp[0][0] = matrix[0][0]

for j in range(1, cols):
    dp[0][j] = dp[0][j - 1] + matrix[0][j]

for i in range(1, rows):
    dp[i][0] = dp[i - 1][0] + matrix[i][0]

for i in range(1, rows):
    for j in range(1, cols):
        dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i][j - 1])

print("\nMinimum Path Cost:", dp[rows - 1][cols - 1])