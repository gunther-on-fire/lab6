'''
fin = open('input.txt')
N = int(fin.readline())
sales = [int(nominal) for nominal in fin.readline().split()]

counter = 0
coins_needed = 0
for sale in sales:
    if sale == 5:
        counter -= 1
    else:
        counter += sale//5 - 1
    if counter > coins_needed:
        coins_needed = counter

fout = open('output.txt', 'w')
print(coins_needed, file = fout)
fout.close()
'''
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
