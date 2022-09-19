import hashlib
from read_data import get_data, Hash

str = 'Somente SHA256 correto'
texts = get_data()


#encode() converts the string into bytes to be accepted by the hash function.
result = hashlib.sha256(str.encode())

#hexidigest() returns the encoded data in hexadecimal format
print('the hexadecimal equivalent of sha256 is : ', result.hexdigest())

#number of hex digits in the string * 4 binary digits = 256
#print(result.block_size)

#bytes
#print(result.digest_size)

hash_object = hashlib.md5(str.encode())
md5_hash = hash_object.hexdigest()
print('the hexadecimal equivalent of md5 is : ', md5_hash)
