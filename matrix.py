# Initial stage of JetBrains Academy numeric matrix processor
# First stage simple matrix addition

matrixA = []
matrixB = []

dimensionsA = input().split()
rows = int(dimensionsA[0])
columns = int(dimensionsA[1])
for i in range(rows):
    new_row = []
    numbers = input().split()
    for num in numbers:
        new_row.append(int(num))
    matrixA.append(new_row)

dimensionsB = input().split()
rows = int(dimensionsB[0])
columns = int(dimensionsB[1])
for i in range(rows):
    new_row = []
    numbers = input().split()
    for num in numbers:
        new_row.append(int(num))
    matrixB.append(new_row)

if dimensionsA != dimensionsB:
    print("ERROR")

else:
    result_matrix = []
    for i in range(rows):
        new_row = []
        for j in range(columns):
            new_row.append(matrixA[i][j] + matrixB[i][j])
        result_matrix.append(new_row)
    for row in result_matrix:
        for num in row:
            print(num, end=" ")
        print()
        

