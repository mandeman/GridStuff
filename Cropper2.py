from PIL import Image

img = Image.open("13691012_1236687019688726_5378317709981582168_o.jpg")

x, y = img.size
wew = min(x, y)

img = img.crop((0, 0, wew, wew))

brack = img.crop((0, 0, wew/2, wew/2))
brack.save("new1.jpg")
brack = img.crop((0, wew/2, wew/2, wew))
brack.save("new2.jpg")
brack = img.crop((wew/2, 0, wew, wew/3))
brack.save("new3.jpg")
brack = img.crop((wew/2, wew/3, wew, 2*wew/3))
brack.save("new4.jpg")
brack = img.crop((wew/2, 2*wew/3, wew, wew))
brack.save("new5.jpg")