from PIL import Image

wallPaper = Image.open("wallPaper.jpg")
square_wallPaper = wallPaper.resize((250, 250))
flip_wallPaper = wallPaper.transpose(Image.FLIP_LEFT_RIGHT)
spin_wallPaper = wallPaper.transpose(Image.ROTATE_90)

wallPaper.show()
square_wallPaper.show()
flip_wallPaper.show()
spin_wallPaper.show()