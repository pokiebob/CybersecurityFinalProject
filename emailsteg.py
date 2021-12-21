import numpy as np
import bitarray

def encode():
	f = open('email1.txt', 'r', encoding='utf-8')
	email = f.read()

	ba = bitarray.bitarray()
	ba.frombytes(email.encode('utf-8'))

	print(ba)




message = "I found a cat yay"
encode()
