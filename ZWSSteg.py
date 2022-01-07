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
	email_array.insert(i, "0")


	#print(email_array)
	
	f = open("encoded.txt", "w")
	counter = 0
	for x in email_array:
		if (x == "0"):
			f.write(u'\u200b\u200b')
			#f.write('!!')
		if (x == "1"):
			f.write(u'\u200b')
			#f.write('!')
		else:
			f.write(to_char(x))
	f.close()
	print("Encoded message!")

#01100001
#zws = '0b11100010', '0b10000000', '0b10001011'

def decode(source):
	f = open(source, 'r', encoding='utf-8')
	email = f.read()
	email_array = to_byte_array(email)

	#print(email_array)

	while('0b10000000' in email_array):
		email_array.remove("0b10000000")
	while('0b10001011' in email_array):
		email_array.remove("0b10001011")
	#print(email_array)

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
	message = message.replace('00000000', '')
	message = message.replace('0100000', '00100000')
	message = message[:-1]
	#print(message)

	message_array = space(message)
	#print(message_array)
	

	for x in message_array:
		if (len(x) < 8):
			break
		print(to_char(x), end="")
	print()

			
#hu!h!uhuhu!huhu
#hu���h���uhuhu���huhu


#De!ar !Stu!yv!esant C!o!mmu!n!ity!,!
#
#!T!h!e! l!e!t!te!r !be!l!ow! !i!s j!u!st !a no!tificat!i!on of! a! confir!m!ed c!a!se!(!s) of! C!O!V!ID!-19.! Additi!o!n!a!l f!ol!l!owup !an!d! !a!cti!on steps will

message = "I found a cat yay"
encode('email1.txt', message)
decode('encoded.txt')