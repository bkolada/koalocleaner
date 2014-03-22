# -*- coding: utf-8 -*-

__author__ = 'Kaef'

class FileNotSelected(ValueError):
    def __init__(self):
        ValueError.__init__(self, "User canceled file selection window")


if __name__ == "__main__":
    a = FileNotSelected()
    print a
