from PIL import Image
from PIL import ImageFilter

wallPaper = Image.open("wallPaper.jpg")
# black_white = wallPaper.convert("L")
# black_white.show()

blur = wallPaper.filter(ImageFilter.BLUR)
detail = wallPaper.filter(ImageFilter.DETAIL)
edges = blur = wallPaper.filter(ImageFilter.FIND_EDGES)
blur.show()
