def removeDuplicates(A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        for j in range(newTail+1, len(A)):
            A.pop(-1)
        return(newTail+1,A)

arr = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(arr))