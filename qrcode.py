import qrcode as q

qr = q.QRCode(
	version=1,
	box_size=20,
	border=5
)

data = input("enter the data or the url which has to be encoded in qr code:")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white') #you can change the background and fill color 
img.save(input("enter the name for qr code:")+'.png')