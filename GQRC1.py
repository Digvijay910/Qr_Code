import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,                                  
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10 , border = 4,)

qr.add_data("https://x.com/DigviijayPatil?t=kwmBV1amNzA2u5kLF7COxQ&s=09")
qr.make(fit = True)
img = qr.make_image(fill_color = "orange" , back_color = "black")

img.save("MY_Twitter_Profile.png")