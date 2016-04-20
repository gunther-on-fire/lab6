
f = open('input.txt')

K, N = map(int, f.readline().split())
M = list(map(int, f.readline().split()))

for i in range(K - 1):
    A = list(map(int, f.readline().split()))
    for j in range(N):
        M[j] = min(M[j], A[j])

f.close()

f = open('output.txt', 'w')

print(" ".join(map(str, M)), file=f)

f.close()
'''
f = open('input.txt')
k, N = map(int, f.readline().split())

B = ['x']*N

for year in range(k):
	A = list(map(int, f.readline().split()))
	for i in range(N):
		if B[i] == 'x' or A[i] < B[i]:
			B[i] = A[i]
f.close()

f = open('output.txt', 'w')
print(B, file=f)
f.close()
'''