import qrcode

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=6,
    border=2,
)

user_input = input("Enter qrcode data here: ")
qr.add_data(user_input)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img = img.convert("L")
# img.show()
img.save("qrcode.png")
