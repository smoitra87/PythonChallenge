import Image

# download the image from: http://www.pythonchallenge.com/pc/return/cave.jpg

image = Image.open("cave.jpg")
nsize = tuple([x / 2 for x in image.size])
odd = even = Image.new(image.mode, nsize)

for x in range(image.size[0]):
    for y in range(image.size[1]):
        if x % 2 == 0 and y % 2 == 0:
            even.putpixel((x / 2, y / 2), image.getpixel((x, y)))
        elif x % 2 == 0 and y % 2 == 1:
            odd.putpixel((x / 2, (y - 1) / 2), image.getpixel((x, y)))
        elif x % 2 == 1 and y % 2 == 0:
            even.putpixel(((x - 1) / 2, y / 2), image.getpixel((x, y)))
        else:
            odd.putpixel(((x - 1) / 2, (y - 1) / 2), image.getpixel((x, y)))

even.save("even.jpg")
odd.save("odd.jpg")