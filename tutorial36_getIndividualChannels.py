from PIL import Image

wallPaper = Image.open("wallPaper.jpg")
# print(wallPaper.mode)   # RGB

# split img into parts
r, g, b = wallPaper.split()
r.show()    # red channel
g.show()
b.show()

# merge effect
# new_img = Image.merge("RGB", (r, g, b))
# new_img.show()

# combine different channels from different imgs
kid = Image.open("837.jpg")
r1, g1, b1 = kid.split()

new_img = Image.merge("RGB", (r1, g, b1))
new_img.show()



