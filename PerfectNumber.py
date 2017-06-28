import sys

def is_perfect(num):
	sum = 0
	for i in [x + 1 for x in range(int(num) / 2)]:
		if int(num) % i == 0:
			sum += i
	return sum == int(num)

for i in sys.argv[1:]:
	print is_perfect(i)