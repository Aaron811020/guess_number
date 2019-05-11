import random

r = random.randint(1,100)
min_num = 1;
max_num = 100;
count = 0;

while True:
	count = count +1
	num = int(input('請猜 %d - %d 數字:' %(min_num, max_num)))
	if num == r:
		print('猜對了, 答案是 %d ,總共猜了 %d 次' %(r, count))
		break
	elif num < r:
		min_num = num+1
	elif num > r:
		max_num = num-1

	