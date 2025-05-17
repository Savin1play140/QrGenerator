import qrcode;from PIL import Image;data=input("data:");size_multiply=1;qr=qrcode.QRCode(version=40,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=2,border=1);qr.add_data(data);qr.make(fit=True);import arcade;img=qr.make_image(fill_color="black",back_color="white");width,height=img.size;arcade.open_window(width*size_multiply,height*size_multiply,"Drawing");arcade.set_background_color(arcade.color.WHITE);arcade.start_render();ascii_qr=[]
for y in range(width):
	for x in range(height):
		pixel=img.getpixel((x,y))
		if pixel==255:
			ascii_qr.append((x,y))
arcade.draw_points(ascii_qr,arcade.color.BLACK,size_multiply);arcade.finish_render();arcade.run()