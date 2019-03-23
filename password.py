password1 = 'a123456'
password2 = input('輸入密碼: ')
i = 3
while True:
	if password1 == password2:
		print('登入成功')
		break
	
	else:
		i = i - 1
		if i == 0:
			print('密碼錯誤')
			print('鎖帳號')
			break
		print('密碼錯誤! 還有', i ,'次機會')
		password2 = input('輸入密碼: ')