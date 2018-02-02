a = [[2,-2], [5,3]]
b = [[5,2], [1,0]]

def mat(a, b):
    put = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        put.append(row)
    return put

print mat(a, b)