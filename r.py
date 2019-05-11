import random

min_num = int(input('輸入猜數字最小值: '))
max_num = int(input('輸入猜數字最大值: '))

r = random.randint(min_num, max_num)
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

	