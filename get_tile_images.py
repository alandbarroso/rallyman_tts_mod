import requests
from PIL import Image
import time

def get_image_download_list():
	# img_list = ["tile-101.webp"]
	img_list = []
	tile_number = 138
	while tile_number <= 150:
		if (tile_number in (102,108,109,110,113,114,118,119,120,123,126) or tile_number >= 128) and tile_number not in (138,): 
			img_list.append("tile-" + str(tile_number) + "a" + ".webp") 
			img_list.append("tile-" + str(tile_number) + "b" + ".webp")
		else:
			img_list.append("tile-" + str(tile_number) + "a" + "-1.webp") 
			img_list.append("tile-" + str(tile_number) + "b" + "-1.webp")

		tile_number = tile_number + 1

	tile_number = 201
	while tile_number <= 232:
		img_list.append("tile-" + str(tile_number) + "a" + ".webp") 
		img_list.append("tile-" + str(tile_number) + "b" + ".webp")

		tile_number = tile_number + 1

	tile_number = 301
	while tile_number <= 326:
		img_list.append("tile-" + str(tile_number) + "a" + ".webp") 
		img_list.append("tile-" + str(tile_number) + "b" + ".webp")

		tile_number = tile_number + 1

	tile_number = 401
	while tile_number <= 415:
		img_list.append("tile-" + str(tile_number) + "a" + ".webp") 
		img_list.append("tile-" + str(tile_number) + "b" + ".webp")

		tile_number = tile_number + 1

	img_list.append("tile-" + str(418) + "a" + ".webp") 
	img_list.append("tile-" + str(418) + "b" + ".webp")

	img_list.append("tile-" + str(419) + "a" + ".webp") 
	img_list.append("tile-" + str(419) + "b" + ".webp")

	return img_list

def download_and_save_img(image_filename):
	hostname = 'https://rekee.net/tiles/'

	image_url = hostname + image_filename

	img_data = requests.get(image_url).content
	f = open('tile_images/webp/' + image_filename, 'wb')
	f.write(img_data)
	f.close()

	i = Image.open('tile_images/webp/' + image_filename).convert('RGB')
	i.save('tile_images/' + image_filename.replace('webp', 'png'), 'png')

img_list = get_image_download_list()
for filename in img_list:
	print('Downloading ' + filename)
	download_and_save_img(filename)
	print('Image saved successfully')
	print('-----------------------------------')

	time.sleep(1)