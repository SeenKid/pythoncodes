import qrcode

img = qrcode.make('URL')
img.save('qrcode.png')
