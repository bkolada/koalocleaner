# -*- coding: utf-8 -*-

__author__ = 'Kaef'

class FileNotSelected(ValueError):
    def __init__(self):
        ValueError.__init__(self, "User canceled file selection window")

class ClearTemporaryFolderFailed(ValueError):
    def __init__(self, dir):
        ValueError.__init__(self, "Script can't remove temporary folder. \nPlease clear content manual.\nPath:\n%s"%dir)


if __name__ == "__main__":
    a = FileNotSelected()
    print a
