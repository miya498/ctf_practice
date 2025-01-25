from Crypto.Util.number import getPrime
from Crypto.Util.number import bytes_to_long, long_to_bytes

flag = b"katagaitai-CTF{RSA}"   #フラグ
m = bytes_to_long(flag)         #フラグを数値に変換

bit_length = 1024
p = getPrime(bit_length)
q = getPrime(bit_length)

N = p*q                         #公開鍵
e = 0x10001                     #公開鍵

phi = (p-1)*(q-1)
d = pow(e,-1,phi)                 #秘密鍵

c = pow(m,e,N)                  #暗号化
print(long_to_bytes(c))
k = pow(c,d,N)                  #復号
print(long_to_bytes(k))
