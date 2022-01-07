def to_byte_array(s):
    s_bytearray = bytearray(s, "utf8")
    s_array = []
    for x in s_bytearray:
        b = bin(x)
        s_array.append(b)
    return s_array


def encode(source, message):
	f = open(source, 'r', encoding='utf-8')
	email = f.read()
	email_array = to_byte_array(email)
	
	total_length = len(email_array)
	message_array = to_byte_array(message)
	message_length = len(message_array)

	if (True):
		print(email_array)
		print(message_array)
		print(total_length)
		print(message_length)

message = "I found a cat yay"
encode('email1.txt', message)




#11100010 10000000 10001011	zws