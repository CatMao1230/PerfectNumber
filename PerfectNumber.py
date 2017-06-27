# encoding: utf-8
def is_perfect(num):
	sum = int(num)
	for i in range(1, int(num) / 2 + 1):
		if int(num) % i == 0:
			sum -= i
	if sum == 0:
		return "True"
	else:
		return "False"


while 1:
	n = raw_input()
	if n != "-1":
		print is_perfect(n)
	else:
		break