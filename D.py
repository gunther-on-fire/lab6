f = open('input.txt')
k = int(fin.readline())
N = int(fin.readline())
f.close()

B = ['x']*N

for year in range(k):
	A = list(map(int, f.readline.split()))
	A = A[:N]
	for i in range(N):
		if B[i] == 'x' or A[i] < B[i]:
			B[i] = A[i]

f.open('output.txt', 'w')
print(B, file=f)
f.close()