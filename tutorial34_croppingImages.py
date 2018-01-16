from PIL import Image

img = Image.open("wallPaper.jpg")
area = (100, 100, 300, 375)
cropped_img = img.crop(area)

img.show()
cropped_img.show()
