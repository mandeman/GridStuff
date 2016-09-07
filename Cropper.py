from PIL import Image

img = Image.open("C:\\Users\\Abhijit\\Desktop\\Wallpaper\\Rabu Raibu Sunshine\\1472475292632.jpg")

x, y = img.size

if(x/y < 1.2):
    while(y > x * 5/6):
        y = y - 0.1*y
    x = 1.2 * y
else:
    while(x > y * 1.2):
        x = x - 0.1 * x
    y = x * 5/6


img2 = img.crop((0, 0, x, y))

#img2.show()

brack = img2.crop((0, 0, x/2, y * 0.6))
brack.save("s1.jpg")
brack = img2.crop((x/2, 0, x, y * 0.6))
brack.save("s2.jpg")
brack = img2.crop((0, y*0.6, x/3, y))
brack.save("s3.jpg")
brack = img2.crop((x/3, y*0.6, 2*x/3, y))
brack.save("s4.jpg")
brack = img2.crop((2*x/3, y*0.6, x, y))
brack.save("s5.jpg")

