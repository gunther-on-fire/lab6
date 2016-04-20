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