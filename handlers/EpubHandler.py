# -*- coding: utf-8 -*-

__author__ = 'Kaef'

from HTMLParser import HTMLParser, starttagopen

class Container:
    def __init__(self, parent=None):
        self.parent = parent
        self.childs = []
        self.tag = None
        self.attr = None
        self.content = None

    def add_child(self):
        self.childs.append(Container(self))
        return self.childs[-1]

class MyHTMLParser(HTMLParser):
    def __init__(self, rep):
        HTMLParser.__init__(self)
        self.consider = False
        self.data = Container()
        self.current = self.data
        self.rep_pattern = rep

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.consider = True
            return
        if self.consider:
            self.current = self.current.add_child()
            self.current.tag = tag
            self.current.attr = attrs

    def handle_endtag(self, tag):
        if tag == "body":
            self.consider = False
            return
        if self.consider:
            self.current=self.current.parent

    def handle_data(self, data):
        if self.consider:
            self.current = self.current.add_child()
            self.current.content = data.replace(self.rep_pattern, "&")
            self.current=self.current.parent


class Parser:
    def get_file_content(self, path ):
        aa = open(path, "rb")
        cont = aa.read()
        cont = cont.replace("&","DHTN__")
        return cont

    def run(self, path):
        parser = MyHTMLParser("DHTN__")
        parser.feed(self.get_file_content(path))
        return parser.data

if __name__ == "__main__":
    pass

