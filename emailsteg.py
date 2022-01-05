import numpy as np
import bitarray
import bitarray.util as bau

def encode(src, message, key):
	f = open(src, 'r', encoding='utf-8')
	email = f.read()
	emailarray = bitarray.bitarray()
	emailarray.frombytes(email.encode('utf-8'))
	emailData = [emailarray[i:i + 8] for i in range(0, len(emailarray), 8)]
	totalBixels = len(emailData)

	ba = bitarray.bitarray()
	ba.frombytes(message.encode('utf-8'))
	requiredBixels = len(ba)

	if requiredBixels > totalBixels:
		print("Error: message too long")
	else:
		mCounter = 0
		for bixel in range(totalBixels):
			if mCounter < requiredBixels:
				emailData[bixel] = int(emailData[bixel].to01()[2:9] + str(int(ba[mCounter])), 2)
				mCounter += 1
		s = ""
		for i in range(len(emailData)):
			print(bitarray.bitarray(emailData[i]).tobytes())

		print(s)




message = "I found a cat yay"
encode('email1.txt', message, '123edsfg554rfghgfdr56uij')
