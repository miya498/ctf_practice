def caesar_cipher_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            plaintext += char
    return plaintext

ciphertext = "Khoor Zruog!"  # シーザー暗号化されたテキスト
for shift in range(26):  # 全シフト値を試す
    print(f"Shift {shift}: {caesar_cipher_decrypt(ciphertext, shift)}")
