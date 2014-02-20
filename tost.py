# -*- coding: utf-8 -*-

__author__ = 'Kaef'

from HTMLParser import HTMLParser, starttagopen

aa = open("Section0001.xhtml", "rb")

cont = aa.read()
cont = cont.replace("&","_")

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
    def __init__(self):
        HTMLParser.__init__(self)
        self.consider = False
        self.data = Container()
        self.current = self.data


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
            print "--%s--"%data.__str__()
            self.current = self.current.add_child()
            self.current.content = data
            self.current=self.current.parent

parser = MyHTMLParser()
parser.feed(cont)
a = parser.data.childs[1]
print a.childs
print a.tag
print a.attr
print "--%s--"%a.content
