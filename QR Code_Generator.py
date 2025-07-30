import qrcode
data = input("enter the text or url to generate QR code: ")
filename = input("enter the filename to save QR code: ")
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code generated and saved as {filename}.")        