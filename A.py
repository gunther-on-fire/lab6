input = open('input.txt', 'r')
output = open('output.txt', 'w')
A = list(map(int, input.readline().split()))

A.sort()
for i in range(len(A)):
	if A[i] == A[i+1]:
		print(A[i])
		break

print(A[i], file=output)