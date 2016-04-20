fin = open('input.txt')
N = int(fin.readline())
A = list(map(int, fin.readline().split()))
fin.close()

min_coins_number = coins_number = 0

for elem in A:
	if elem == 5:
		coins_number += 1
	else:
		coins_number -= int(elem/5-1)
	if coins_number < min_coins_number:
		min_coins_number = coins_number

fout = open('output.txt', 'w')
if min_coins_number < 0:
	print(-min_coins_number, file=fout)
else:
	print(0, file=fout)
fout.close()
