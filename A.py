input = open('input.txt', 'r')
output = open('output.txt', 'w')
A = list(map(int, input.readline().split()))

A.sort()
for i in range(len(A)):
	if A[i+1] == A[i]:
		print(A[i])
		break

print(A[i], file=output)
input.close()
output.close()