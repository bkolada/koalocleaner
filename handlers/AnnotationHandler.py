__author__ = 'kolada'

import xml.etree.ElementTree as ET

class AnnotationHandler:
    def __init__(self):
        self.annot_long = "{http://ns.adobe.com/digitaleditions/annotations}annotation"
        self.target_long = "{http://ns.adobe.com/digitaleditions/annotations}target"
        self.fragment_long = "{http://ns.adobe.com/digitaleditions/annotations}fragment"

    def get_start(self, attr):
        lev1 = attr.split("#")
        lev2 = lev1[1].strip("(point)/").split(":")
        lev2a = lev2[0].split("/")
        return lev1[0], lev2a, lev2[1]

    def get_fragment_fields_from_target(self, target):
        for i  in target:
            print i
        fragment = target.find(self.fragment_long)
        print "o",fragment,  self.get_start(fragment.attrib["start"])

    def get_target_from_child(self, child):
        return child.find(self.target_long)

    def add_annotation_from_child(self,child):
        print child
        target = self.get_target_from_child(child)
        print self.get_fragment_fields_from_target(target)

    def parse_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        for child in root.findall(self.annot_long):
            self.add_annotation_from_child(child)


if __name__  == "__main__":
    a = AnnotationHandler()
    a.parse_xml("../test.epub.annot")


    #dupa