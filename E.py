f = open('input.txt')

N, k = map(int, f.readline().split())

A = [0]*N

for i in range(k):
	B = list(map(int,f.readline().split()))
	A[(B[0] - 1)] -= B[2]
	A[(B[1] - 1)] += B[2]

f.close()

f = open('output.txt', 'w')
print(A, file=f)
f.close()