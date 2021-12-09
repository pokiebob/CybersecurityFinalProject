import bitarray
import base64

message = 'I finally finished all my math homework.'

ba = bitarray.bitarray()
ba.frombytes(message.encode('utf-8'))
print(ba)