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
    return image.filter(ImageFilter.CONTOUR)

def edgeenhance(image):
    return image.filter(ImageFilter.EDGE_ENHANCE_MORE)


def emboss(image):
    return image.filter(ImageFilter.EMBOSS)


def findedges(image):
    return image.filter(ImageFilter.FIND_EDGES)


def blur(image):
    many = 5
    return image.filter(ImageFilter.GaussianBlur(many)).convert('RGB')


def smooth(image):
    return image.filter(ImageFilter.SMOOTH_MORE)

#import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lenovo\AppData\Local\Tesseract-OCR\tesseract'

#print(pytesseract.image_to_string(r'C://Users//lenovo//Desktop//Screenshot 2020-09-29 133100.png', lang='fas').strip())'''