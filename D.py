f = open('input.txt')

k, N = map(int, f.readline().split())
M = list(map(int, f.readline().split()))

for i in range(k - 1):
    A = list(map(int, f.readline().split()))
    for j in range(N):
        M[j] = min(M[j], A[j])

f.close()

f = open('output.txt', 'w')

print(" ".join(map(str, M)), file=f)

f.close()