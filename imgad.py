from PIL import Image
from PIL import ImageFilter, ImageEnhance

with Image.open('image.png') as picture:
    print('Розмір зображення', picture.size)
    print('Формат зображення', picture.format)
    print('Тип зображення:', picture.mode)
    picture.show()


    grey = picture.convert('L')
    grey.save('grey.png')
    grey.show()

    rotated = picture.transpose(Image.ROTATE_180)
    rotated.save('rotated.png')
    rotated.show()

    flipped = grey.transpose(Image.FLIP_LEFT_RIGHT)
    flipped.save('flipped.png')
    flipped.show()

    contrast = ImageEnhance.Contrast(picture)
    contrast = picture.enhance(14.88)
    contrast.save('contrast.png')
    contrast.show()