import os
from pathlib import Path

# TODO: separate file to different folder
SUBDIRECTORIES = {
    'DOCUMENTS': ['.pdf','.rtf','.txt'],
    'AUDIO': ['.m4a','.m4b','.mp3'],
    'VIDEOS': ['.mov','.avi','.mp4'],
    'IMAGES': ['.jpg','.jpeg','.png']
}


def pickDirectory(value):
    # TODO: category is a Folder name, suffixes is a file names
    for category, suffixes in SUBDIRECTORIES.items():
        # TODO: get the folder name when correct file match with suffixes
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'

print(pickDirectory('.pdf'))


def organizeDirectory():
    # TODO: scandir() - scan directory
    for item in os.scandir():
        # TODO: skip item if it is directory already
        if item.is_dir():
            continue
        # TODO: get path
        filePath = Path(item)
        print('File Path: ', filePath)
        # TODO: get type of file, after pointer
        filetype = filePath.suffix.lower()
        print('File type: ', filetype)
        # TODO: get the directory base on filetype
        directory = pickDirectory(filetype)
        print('Directory: ', directory)
        directoryPath = Path(directory)
        print('Directory Path: ', directoryPath)
        if directoryPath.is_dir() != True:
            # TODO: mkdir is creating folder syntax
            directoryPath.mkdir()
        # TODO: rename the filePath
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()