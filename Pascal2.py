def getRow(rowIndex):
    rt=[1]*(rowIndex+1)
    print(rt)
    for i in range(2, rowIndex+1):
        for j in range(1, i):
            rt[i-j]+=rt[i-j-1]
    #return rt

print(getRow(3))