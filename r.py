import random

r = random.randint(1,100)
min_num = 1;
max_num = 100;
while True:
	num = int(input('請猜數字 1-100 :'))
	if num == r:
		print('猜對了, 答案是', r)
		break
	elif num < r:
		min_num = num+1
	elif num > r:
		max_num = num-1

	print('請猜 %d - %d 數字' %(min_num, max_num))