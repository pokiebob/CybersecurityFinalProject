import bitarray
import numpy as np
from PIL import Image

def encodeImg(src, location, message, key):
	img = Image.open(src, 'r').convert('RGB')
	width, height  = img.size
	imgData = np.array(list(img.getdata()))
	# print(img.mode)
	print(imgData)

	totalPixels = imgData.size // 3
	# print(totalPixels)

	message += key
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
		newImg.save(location)
		print('yay')

def decodeImg(src, key):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
	    if message[-1 * len(key):] == key:
	        break
	    else:
	        message += chr(int(hidden_bits[i], 2))
    if key in message:
        print("Hidden Message:", message[:-1 * len(key)])
    else:
        print("No Hidden Message Found")

key = "sjae89j89k9k90grjkd9gjs89"
message = "I finally finished all my math homework."
# encodeImg('grumpycat.jpg', 'lsb_grumpycat.jpg', message, key)
# decodeImg('lsb_grumpycat.jpg', key)

encodeImg('grumpycat.png', 'lsb_grumpycat.png', message, key)
decodeImg('lsb_grumpycat.png', key)