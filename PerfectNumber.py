import sys

def is_perfect(num):
	sum = 0
	for i in range(1, int(num) / 2 + 1):
		if int(num) % i == 0:
			sum += i
	return sum == int(num)

for i in range(1, len(sys.argv)):
	print is_perfect(int(sys.argv[i]))