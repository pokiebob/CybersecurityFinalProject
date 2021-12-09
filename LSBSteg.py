import bitarray
import numpy as np
from PIL import Image

message = 'I finally finished all my math homework.'

# im = Image.open('grumpycat.jpg')
# im.save('lsb_grumpycat.jpg')

def encodeImg(src, message):
	img = Image.open(src, 'r')
	width, height  = img.size
	imgData = np.array(list(img.getdata()))
	print(img.mode)
	print(imgData)

	totalPixels = imgData.size // 3
	print(totalPixels)

	ba = bitarray.bitarray()
	ba.frombytes(message.encode('utf-8'))
	print(len(ba))

	if len(ba) > totalPixels:
		print("Error: message too long")
	else:
		a = int(bin(imgData[1][1])[2:9] + int(ba[0]), 2)
		print(a)

encodeImg('grumpycat.jpg', message)