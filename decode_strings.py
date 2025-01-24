import base64
import codecs

# Base64デコード
encoded = "SGVsbG8gV29ybGQh"
decoded = base64.b64decode(encoded).decode()
print(f"Base64 Decoded: {decoded}")

# Hexデコード
hex_encoded = "48656c6c6f20576f726c6421"
decoded = bytes.fromhex(hex_encoded).decode()
print(f"Hex Decoded: {decoded}")

# ROT13デコード
rot13_encoded = "Uryyb Jbeyq!"
decoded = codecs.decode(rot13_encoded, 'rot_13')
print(f"ROT13 Decoded: {decoded}")
