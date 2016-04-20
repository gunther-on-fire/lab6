f = open('input.txt')

N = int(f.readline())
A = list(map(int, f.readline().split()))
f.close()

min_dist = dist = N

for i in range(N):
	
	if A[i] < 0:
		for j in range(i+1,N):
			if -A[i] == A[j]:
				dist = j - i

	if dist < min_dist:
		min_dist = dist

f = open('output.txt', 'w')
print(0 if min_dist == N else min_dist, file=f)
f.close()
