import qrcode

qr_img = qrcode.make("Hello Good Morning")

qr_img.save("qr-img.jpg")