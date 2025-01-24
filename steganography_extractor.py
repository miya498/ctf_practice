from PIL import Image

def extract_lsb(image_path):
    img = Image.open(image_path)
    binary_data = ""
    for pixel in img.getdata():
        binary_data += str(pixel[0] & 1)  # 赤成分の最下位ビットを抽出
    return ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))

hidden_message = extract_lsb("steg_image.png")
print(f"Hidden Message: {hidden_message}")
