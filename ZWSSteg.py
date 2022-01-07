def to_byte_array(s):
	s_bytearray = bytearray(s, "utf8")
	s_array = []
	for x in s_bytearray:
		b = bin(x)
		s_array.append(b)
	return s_array


def to_char(binary_string):
	i = int(binary_string, 2)
	c = chr(i)
	return c


def encode(source, message):
	f = open(source, 'r', encoding='utf-8')
	email = f.read()
	email_array = to_byte_array(email)
	message_array = to_byte_array(message)

	message_binary = []
	for x in message_array:
		for i in range(len(x)-1):
			if (i >= 1):
				i += 1
			message_binary.append(x[i])	
	
	i = 1
	for x in message_binary:
		if (int(x)):
			email_array.insert(i, "1")
			i += 1
		i += 1
	#print(email_array)
	
	f = open("new.txt", "w")
	for x in email_array:
		if (x == "1"):
			#f.write(u'\u200b')
			f.write('!')
		else:
			f.write(to_char(x))
	f.close()




message = "I found a cat yay"
encode('email1.txt', message)
