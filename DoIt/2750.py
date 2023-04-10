N = int(input())
A = [0]*N


for i in range(0, N):
    for j in range(0, N-1):
        if A[j] < A[i]:
            A[j] = A[i]
    print("~~~", A)
