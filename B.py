f = open('input.txt')
A = list(map(int, f.readline().split()))
f.close()

min_coins_number = coins_number = 0

for elem in A:
	if elem == 5:
		coins_number += 1
	else:
		coins_number -= int(elem/5-1)
	if coins_number < min_coins_number:
		min_coins_number = coins_number

f = open('output.txt', 'w')
if min_coins_number < 0:
	print(abs(min_coins_number), file=f)
else:
	print(0, file=f)
f.close()
