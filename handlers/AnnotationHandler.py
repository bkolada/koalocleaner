__author__ = 'kolada'

import xml.etree.ElementTree as ET

class AnnotationHandler:
    def __init__(self):
        self.annot_long = "{http://ns.adobe.com/digitaleditions/annotations}annotation"
        self.target_long = "{http://ns.adobe.com/digitaleditions/annotations}target"
        self.content_long = "{http://ns.adobe.com/digitaleditions/annotations}content"
        self.text_long = "{http://ns.adobe.com/digitaleditions/annotations}text"
        self.fragment_long = "{http://ns.adobe.com/digitaleditions/annotations}fragment"
        self.annotations = []

    def get_start(self, attr):
        lev1 = attr.split("#")
        lev2 = lev1[1].strip("(point)/").split(":")
        lev2a = lev2[0].split("/")
        return lev1[0], lev2a, lev2[1]

    def get_end(self, attr):
        lev1 = attr.split("#")
        lev2 = lev1[1].strip("(point)/").split(":")
        lev2a = lev2[0].split("/")
        return lev1[0], lev2a, lev2[1]

    def get_fragment_fields_from_target(self, target):
        fragment = target.find(self.fragment_long)
        start = self.get_start(fragment.attrib["start"])
        end = self.get_start(fragment.attrib["end"])
        text = fragment.find(self.text_long)
        return start, end, text.text

    def get_target_from_child(self, child):
        return child.find(self.target_long)

    def add_annotation_from_child(self,child):
        target = self.get_target_from_child(child)
        destination = self.get_fragment_fields_from_target(target)
        comment = child.find(self.content_long).find(self.text_long)
        self.annotations.append([destination[0], destination[1], destination[2], comment.text])

    def parse_xml(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        for child in root.findall(self.annot_long):
            self.add_annotation_from_child(child)

    def get_annotations(self):
        return self.annotations

    def iterate_over_annotations(self):
        for i in self.annotations:
            yield i
        return

if __name__  == "__main__":
    a = AnnotationHandler()
    a.parse_xml("../test.epub.annot")
    for i in a.iterate_over_annotations():
        print i

    #dupa