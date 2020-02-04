# Warshall's algorithm
matrix = [[0,1,0,0],
     [0,0,1,0],
     [0,0,0,1],
     [0,0,0,0]
    ]
for k in range(0,4):
    for i in range(0,4):
        for j in range(0,4):
            if(matrix[i][k] == matrix[k][j] and
               1 == matrix[i][k] and
               1 == matrix[k][j]):
                matrix[i][j] = 1


for k in range(0,4):
    print(matrix[k])
