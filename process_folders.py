from os import listdir
from os.path import isfile, join


def isImage(file):
    try:
        bits = file.split(".")
        extension = bits[len(bits)-1]
        if extension == "png":
            return True
        return False
    except IndexError:
        return False


def getFileAddresses(folder):
    filenames = []
    for file in listdir(folder):
        if isfile(join(folder, file)):
            if isImage(file):
                filenames.append(join(folder, file))
    return filenames

