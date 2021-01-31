# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確就印出 "登入成功!"
# 如果不正確就印出 "密碼錯誤! 還有__次機會!"
x = 0
while True:
	password = input('請輸入密碼: ')
	if password != 'a123456':
		x = x + 1
		y = 3 - x
		print('密碼錯誤!，還有', y, '次機會!')
		if x >= 3:
			break
	else:
		print('登入成功!')
		break
		

