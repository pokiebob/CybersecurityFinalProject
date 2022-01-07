import sys

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

def space(binary):
	length = len(binary)
	binary_array = []
	while (len(binary) > 0):
		binary_array.append(binary[0:8])
		binary = binary[8:]
	return binary_array

def encode(source, message):
	f = open(source, 'r', encoding='utf-8')
	email = f.read()

	if len(email) < len(message):
		print("Message exceeds length of email")

	else:
		email_array = to_byte_array(email)
		message_array = to_byte_array(message)

		#print(message_array)
		message_binary = []
		for x in message_array:
			if (len(x)<=8):
				 x = "0" * (9-len(x)) + x
			for i in range(len(x)):
				if (x[i] != 'b'):
					message_binary.append(x[i])	
		#print(message_binary)
		
		i = 1
		for x in message_binary:
			if (int(x)):
				email_array.insert(i, "1")
				i += 1
			i += 1
		email_array.insert(i, "0")
		#print(email_array)
		
		f = open("encoded.txt", "w", encoding="utf-8")
		for x in email_array:
			if (x == "0"):
				f.write(u'\u200D\u200D')
				#f.write('!!')
			elif (x == "1"):
				f.write(u'\u200D')
				#f.write('!')
			elif (x == '0b11100010' or x == '0b10010111' or x == '0b10001111'):
				if (x == '0b11100010'):
					f.write(u'\u25CF')
			else:
				f.write(to_char(x))
		f.close()
		print("Encoded successfully into encoded.txt!")

#01100001
#zws = '0b11100010', '0b10000000', '0b10001011'

def decode(source):
	f = open(source, 'r', encoding='utf-8')
	email = f.read()
	email_array = to_byte_array(email)

	#'0b11100010', '0b10000000', '0b10001101'
	while('0b10000000' in email_array):
		email_array.remove("0b10000000")
	while('0b10001101' in email_array):
		email_array.remove("0b10001101")
	# print(email_array)

	message_array = []
	previous = 0
	for x in email_array:
		#0b100001		!
		#0b11100010		ZWS
		if (x != '0b11100010'):
			if (previous != '0b11100010' and previous != '0' and previous != 0):
				message_array.append('0')
		elif (previous == '0b11100010'):
			break
		else:
			message_array.append('1')
		previous = x
	#print(message_array)

	message = ""
	for x in message_array:
		message += x
	#print(message)
	message = message[:-1]

	# print(message_array)
	message_array = space(message)
	#print(message_array)
	

	for x in message_array:
		print(to_char(x), end="")


if (len(sys.argv) < 3):
	print("Usage: python3 ZWSSteg.py encode text_file message or python3 ZWSSteg.py decode text_file")
elif (sys.argv[1] == 'encode'):
	if (len(sys.argv) < 4):
		print("Error: Encoding requires three arguments.")
	else:
		encode(sys.argv[2], sys.argv[3])
elif (sys.argv[1] == 'decode'):
	decode(sys.argv[2])