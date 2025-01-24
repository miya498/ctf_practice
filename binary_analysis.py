with open("file.bin", "rb") as f:
    data = f.read()

# データの最初の16バイトを表示
print(data[:16])

# XOR解析
key = 0x42
decoded = bytes([b ^ key for b in data])
print(decoded[:16])
