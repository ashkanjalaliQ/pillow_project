from PIL import ImageOps, ImageChops

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