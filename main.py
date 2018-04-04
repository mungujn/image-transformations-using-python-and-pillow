from process_folders import getFileAddresses
from transform_images import performTransformationSet, performTransformationSetWithBlurAndSharpen, openImageFile, \
    modifyFileName, resize

base_directory = "D:\\data\\"


training_folder = base_directory + "training"
training_labels_folder = base_directory + "training labels"
training_images = getFileAddresses(training_folder)
training_labels = getFileAddresses(training_labels_folder)


#  incase you have some images you dont want to or cant sharpen
def fakeSharpenLabel(filename):
    input_image = openImageFile(filename)
    output_image = input_image
    output_filename, extension = modifyFileName(input_image, "_S2")
    output_image.save(output_filename, extension)


#  incase you have some images you dont want to or cant blur
def fakeBlurLabel(filename):
    input_image = openImageFile(filename)
    output_image = input_image
    output_filename, extension = modifyFileName(input_image, "_B0")
    output_image.save(output_filename, extension)


def transform():
    for address in training_labels:
        performTransformationSet(address)
        fakeBlurLabel(address)
        fakeSharpenLabel(address)

    for address in training_images:
        performTransformationSetWithBlurAndSharpen(address)


def resizeAll():
    folders = [base_directory + "training", base_directory + "testing", base_directory + "training labels", base_directory + "testing labels"]

    for folder in folders:
        files = getFileAddresses(folder)
        for file in files:
            resize(file)

resizeAll()
