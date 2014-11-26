input = open("problem8.txt", "r")

total = ""

for line in input:
	total += line.strip(' \t\n\r')

product = 0
for i in range(0, len(total)-12):
	temp = 1
	for j in range(0, 13):
		if(int(total[i + j]) == 0):
			break
		temp *= int(total[i+j])

	product = temp if temp > product else product

print product