import os
from jsonLoader import jsonLoader
from parserPack import parserChoice


def main():
    # Шаблон на имя группы

    # listOfFiles = os.listdir("C:\Test\schedule")
    for dir_, subDirs, files in os.walk("Test\_schedule"):
        if not files:
            continue
        parserChoice(dir_, files)
    return

    #  jsonLoader.uploadJson()


main()
jsonLoader.uploadJson()