# need to install Pillow package first
from PIL import Image

img = Image.open("wallPaper.jpg")
# print image's properties
print(img.size)
print(img.format)

img.show()  # open in a img editor