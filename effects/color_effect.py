from PIL import ImageOps, ImageChops, ImageFilter

def gray_scale(image):
    image = ImageOps.grayscale(image)
    image = image.convert('RGB')
    return image

def b_and_w(image):
    gray = image.convert('L')
    image = gray.point(lambda x: 0 if x < 128 else 255, '1')
    image = image.convert('RGB')
    return image

def negative(image):
    image = ImageChops.invert(image)
    image = image.convert('RGB')
    return image


def contourfilter(image):
    return image.filter(ImageFilter.CONTOUR).convert('RGB')

def edgeenhance(image):
    return image.filter(ImageFilter.EDGE_ENHANCE_MORE).convert('RGB')


def emboss(image):
    return image.filter(ImageFilter.EMBOSS).convert('RGB')


def findedges(image):
    return image.filter(ImageFilter.FIND_EDGES).convert('RGB')


def blur(image):
    many = 5
    return image.filter(ImageFilter.GaussianBlur(many)).convert('RGB')


def smooth(image):
    return image.filter(ImageFilter.SMOOTH_MORE).convert('RGB')

def halftone(img, sample, scale, angle=45):
    img_grey = img.convert('L')  
    channel = img_grey.split()[0]  
    channel = channel.rotate(angle, expand=1)
    size = channel.size[0]*scale, channel.size[1]*scale

    bitmap = Image.new('1', size)
    draw = ImageDraw.Draw(bitmap)

    for x in range(0, channel.size[0], sample):
        for y in range(0, channel.size[1], sample):
            box = channel.crop((x, y, x+sample, y+sample))
            mean = ImageStat.Stat(box).mean[0]
            diameter = (mean/255) ** 0.5
            edge = 0.5 * (1-diameter)
            x_pos, y_pos = (x+edge) * scale, (y+edge) * scale
            box_edge = sample * diameter * scale
            draw.ellipse((x_pos, y_pos, x_pos+box_edge, y_pos+box_edge), fill=255)

    bitmap = bitmap.rotate(-angle, expand=1)
    width_half, height_half = bitmap.size
    xx = (width_half - img.size[0]*scale) / 2
    yy = (height_half - img.size[1]*scale) / 2
    bitmap = bitmap.crop((xx, yy, xx + img.size[0]*scale,
                                  yy + img.size[1]*scale))
    return Image.merge('1', [bitmap])
#import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lenovo\AppData\Local\Tesseract-OCR\tesseract'

#print(pytesseract.image_to_string(r'C://Users//lenovo//Desktop//Screenshot 2020-09-29 133100.png', lang='fas').strip())'''
