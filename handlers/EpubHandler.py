# -*- coding: utf-8 -*-

__author__ = 'Kaef'

from HTMLParser import HTMLParser, starttagopen
from codecs import open as copen

class Container:
    def __init__(self, parent=None):
        self.parent = parent
        self.childs = []
        self.tag = None
        self.attr = None
        self.content = None
        self.old_content = None
        self.exception = ["br"]
    def add_child(self):
        self.childs.append(Container(self))
        return self.childs[-1]

    def get_content(self,id):
        # print id[0], self.childs
        if len(id)>0:
            return self.childs[id[0]-1].get_content(id[1:])
        # print self.tag
        return self.content

    def set_content(self,id, cont):
        if len(id)>0:
            return self.childs[id[0]-1].set_content(id[1:], cont)
        # self.old_content = self.content
        self.content = cont
        print self.content

    def prepare_begining_tag(self):
        attr = ""
        if self.attr:
            for i in self.attr:
                attr+=' %s="%s"'%i
        if self.tag in self.exception:
            return "<%s%s/>"%(self.tag, attr)
        return "<%s%s>"%(self.tag, attr)

    def to_output(self):
        c = ""

        if self.tag is not None:
            c = self.prepare_begining_tag()
            if "/>" in c:
                return c

        for i in self.childs:
            c+=i.to_output()

        if self.content is not None:
            return c+self.content
        if self.tag is not None:
            return c+"</%s>"%self.tag
        return c

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
            # print ">",self.current.content,"<"
            self.current=self.current.parent

class EpubParser:
    def get_file_content(self, path ):
        # aa = open(path, "rb")
        aa = copen(path, "rb",encoding="U8")
        cont = aa.read()
        # cont = cont.replace("&nbsp;"," ")
        cont = cont.replace("&","DHTN__")
        return cont

    def parse(self, path):
        parser = MyHTMLParser("DHTN__")
        parser.feed(self.get_file_content(path))
        return parser.data

class EpubExport:
    def __init__(self):
        self.content = ""

    def read_begining(self, path):
        cont = copen(path, "rb",encoding="U8")
        for i in cont.readlines():
            self.content+=i
            if "body" in i:
                return

    def export_container_to_file(self, path, container):
        self.read_begining(path)
        c = container.to_output()
        # print c
        self.content += c
        self.content +="""</body>
</html>"""

        cont = copen(path, "wb",encoding="U8")
        cont.write(self.content)

if __name__ == "__main__":
    fn = r"C:\Users\Kaef\PycharmProjects\koalocleaner\tmp_epub\OEBPS\Text\Section0001a.xhtml"
    e = EpubParser()
    c = e.parse(fn)
    # c.get_content([1,1,0,0])
    c.set_content([4,1],'Dupa')
    # print c.get_content([4,1])[40:45]
    # print c.get_content([2,2,1])[12:17]
    # print c.get_content([2,2,1])[415:426]
    # c.get_content([5,0,0])
    fn = r"C:\Users\Kaef\PycharmProjects\koalocleaner\tmp_epub\OEBPS\Text\Section0001.xhtml"
    ee = EpubExport()
    ee.export_container_to_file(fn, c)
    # [1].childs[1].tag
