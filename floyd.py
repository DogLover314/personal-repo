# Floyd's algorithm
INF = 999
matrix = [[0,2,2,INF],
     [INF,0,2,3],
     [INF,INF,0,2],
     [INF,INF,INF,0]
    ]

p = [[0 for i in range(4)] for n in range(4)]

for k in range(0,4):
    for i in range(0,4):
        for j in range(0,4):
            if((matrix[i][k] + matrix[k][j]) < matrix[i][j]):
                matrix[i][j] = matrix[i][k] + matrix[k][j]
                p[i][j] = k + 1


print("adjacency matrix")
for k in range(0,4):
    print(matrix[k])

print("path matrix")
for k in range(0,4):
    print(p[k])
