from PIL import Image

im = Image.open('test1.png')

#converting image to RGB values
rgb_im = im.convert('RGB')
#rgb values at coordinate 1, 1
r, g, b = rgb_im.getpixel((1, 1))
print(r, g, b)
