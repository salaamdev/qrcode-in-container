import os

import qrcode

# Generate QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=6,
    border=2,
)

qr.add_data("https://www.salaam.dev")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save QR Code to the /app directory inside the container
output_path = "qrcode.png"
img.save(output_path)

# Print file location to confirm it's saved
print(f"QR Code saved at: {output_path}")
