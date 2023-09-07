from PIL import Image, ImageEnhance, ImageFilter
import os

# Put some images on path and edited images will be put on pathOut
path = './imgs'
pathOut = './editedImgs'

for filename in os.listdir(path):
    img = Image.open(f'{path}/{filename}')
    edit = img.filter(ImageFilter.SHARPEN).convert(
        'L').rotate(90)  # rotates and blacks the photo
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)  # adds contrast to the photo
    clean_name = os.path.splitext(filename)[0]
    edit.save(f'{pathOut}/{clean_name}_edited.jpg')
