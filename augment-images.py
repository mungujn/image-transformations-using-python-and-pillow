from PIL import Image


def openImageFile(filename):
    return Image.open(filename)


def saveImageFile(file, file_type):
    try:
        file.save(file, file_type)
    except IOError:
        print("Error ", IOError)


def modifyFileName(image, add):
    arr = image.filename.split('.')
    return arr[0] + add + "." + arr[1], arr[1]


def flipLeftToRight(filename):
    input_image = openImageFile(filename)
    output_image = input_image.transpose(Image.FLIP_LEFT_RIGHT)
    output_filename, extension = modifyFileName(input_image, "_FLR")
    output_image.save(output_filename, extension)


def flipTopToBottom(filename):
    input_image = openImageFile(filename)
    output_image = input_image.transpose(Image.FLIP_TOP_BOTTOM)
    output_filename, extension = modifyFileName(input_image, "_FTB")
    output_image.save(output_filename, extension)


def rotate90(filename):
    input_image = openImageFile(filename)
    output_image = input_image.transpose(Image.ROTATE_90)
    output_filename, extension = modifyFileName(input_image, "_R90")
    output_image.save(output_filename, extension)


def rotate180(filename):
    input_image = openImageFile(filename)
    output_image = input_image.transpose(Image.ROTATE_180)
    output_filename, extension = modifyFileName(input_image, "_R180")
    output_image.save(output_filename, extension)


def rotate270(filename):
    input_image = openImageFile(filename)
    output_image = input_image.transpose(Image.ROTATE_270)
    output_filename, extension = modifyFileName(input_image, "_R270")
    output_image.save(output_filename, extension)


def performTransformationSet(filename):
    flipLeftToRight(filename)
    flipTopToBottom(filename)
    rotate90(filename)
    rotate180(filename)
    rotate270(filename)

performTransformationSet("coins.jpeg")
"""


"""
