def pe206():
	program_start = datetime.datetime.now()
	max_target = 19293949596979899	# 1.2.3.4.5.6.7.8.900 - will always be 00, so we can drop the 00 to shorten the search space
	min_target = 10203040506070809
	end = int(max_target**0.5)
	start = int(min_target**0.5)/10*10+3
	i = start
	while i <= end:
		curr = i**2
		if str(curr)[::2] == '123456789':
			print i*10
			break
		if str(i)[-1] == '3':	# target ends in 9, so our answer has to end in 3 or 7
			i += 4
		else:
			i += 6
	print datetime.datetime.now() - program_start
	
pe206()
