import os
import qrcode
from PIL import Image

def ipToLink(ip=None, port=None):
    return 'http://'+ip+':'+port+'/'
def ipToFilename(ip=None, port=None):
    return ip.replace('.', '')+port+'.png'

def linkToQR(filename=None, link=None):
    if not os.path.exists(filename):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)

def makeQR(ip=None, port=None):
    link = ipToLink(ip, port)
    filename = ipToFilename(ip, port)
    linkToQR(filename, link)
    return {'link': link, 'filename': filename}

