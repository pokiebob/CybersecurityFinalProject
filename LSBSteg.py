import bitarray
import numpy as np
from PIL import Image

message = 'I finally finished all my math homework.'

# im = Image.open('grumpycat.jpg')
# im.save('lsb_grumpycat.jpg')

def encodeImg(src, message):
	img = Image.open(src, 'r').convert('RGB')
	width, height  = img.size
	imgData = np.array(list(img.getdata()))
	print(img.mode)
	print(imgData)

	totalPixels = imgData.size // 3
	print(totalPixels)

	ba = bitarray.bitarray()
	ba.frombytes(message.encode('utf-8'))
	requiredPixels = len(ba)

	if requiredPixels > totalPixels:
		print("Error: message too long")
	else:
		mCounter = 0
		for row in range(totalPixels):
			for col in range(0, 3):
				if mCounter < requiredPixels:
					imgData[row][col] = int(bin(imgData[row][col])[2:9] + str(int(ba[mCounter])), 2)
					mCounter += 1
		# print(imgData)

		newImgData = imgData.reshape(height, width, 3)
		newImg = Image.fromarray(newImgData.astype('uint8'), img.mode)
		newImg.save('lsb_grumpycat.png')
		print('yay')



encodeImg('grumpycat.png', message)