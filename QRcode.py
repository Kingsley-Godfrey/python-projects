import qrcode

data = input('enter the text or URL: ')
filename = input('enter the filename: ')

img = qrcode.make(data)

img.save(filename)

print(f'QR code saved as {filename}')