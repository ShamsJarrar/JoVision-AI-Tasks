from PIL import Image

def color_to_black(pic_path):

    pic = Image.open(pic_path)

    pixelAccessObj = pic.load()
    w, h = pic.size

    for i in range(w):
        for j in range(h):
            R, G, B = pixelAccessObj[i, j]

            L = int(R * (299/1000) + G * (587/1000) + B * (114/1000))

            pixelAccessObj[i, j] = (L, L, L)
    
    pic.show()


color_to_black(r"Resources\sunflower.jpg")
