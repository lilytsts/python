from PIL import Image, ImageFilter

before = Image.open("sample.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.bmp")
