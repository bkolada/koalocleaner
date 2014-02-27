__author__ = 'kolada'

import xml.etree.ElementTree as ET

class AnnotationHandler:
    def __init__(self):
        pass

    def parse_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        print root

if __name__  == "__main__":
    a = AnnotationHandler()
    a.parse_xml("../test.epub.annot")


    #dupa