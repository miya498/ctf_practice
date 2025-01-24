from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# 鍵生成
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# 暗号化
def rsa_encrypt(public_key, plaintext):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return binascii.hexlify(ciphertext).decode()

# 復号
def rsa_decrypt(private_key, ciphertext):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(binascii.unhexlify(ciphertext))
    return plaintext.decode()

# 実行例
if __name__ == "__main__":
    # 鍵生成
    private_key, public_key = generate_rsa_keys()
    print("Private Key:")
    print(private_key.decode())
    print("\nPublic Key:")
    print(public_key.decode())

    # テスト用データ
    plaintext = "This is a secret message"
    print(f"\nPlaintext: {plaintext}")

    # 暗号化
    ciphertext = rsa_encrypt(public_key, plaintext)
    print(f"\nCiphertext: {ciphertext}")

    # 復号
    decrypted_text = rsa_decrypt(private_key, ciphertext)
    print(f"\nDecrypted Text: {decrypted_text}")
