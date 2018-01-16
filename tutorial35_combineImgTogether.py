from PIL import Image

wallPaper = Image.open('wallPaper.jpg')
kid = Image.open("837.jpg")

area = (100, 100, 300, 300)
# call paste function to paste kid img on top of wall paper img
wallPaper.paste(kid, area)

wallPaper.show()
