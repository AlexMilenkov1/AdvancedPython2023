n = int(input())

matrix = [[int(x) for x in input().split()] for rows in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][(n - i) - 1] for i in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
