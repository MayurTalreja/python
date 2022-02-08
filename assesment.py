import csv
import json


class Node(object):
    def __init__(self, name, id,url):
        self.name = name
        self.children = []
        self.url = url
        self.id = id

    def child(self, cname,cid, url):
        child_found = [c for c in self.children if c.name == cname]
        if not child_found:
            _child = Node(cname,cid,url)
            self.children.append(_child)
        else:
            _child = child_found[0]
        return _child

    def as_dict(self):
        res = {}
        # res = {'Label': self.name}
        # res['Label']=self.name
        # res['ID']=self.id
        # res['link'] = self.url
        # res['children'] = [c.as_dict() for c in self.children]
        if self.name != '':
            res['Label']=self.name
            res['ID']=self.id
            res['link'] = self.url
            res['children'] = [c.as_dict() for c in self.children]
        return res


root = Node('NA','NA','NA') 

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    #reader.next()
    for index,row in enumerate(reader):
        grp1, grp2, grp3,grp4,grp5,grp6,grp7,grp8,grp9, url = row #adding grp4 onwords
        if index == 1:
            root = Node(grp2,grp3,grp4)
        root.child(grp5,grp6,grp7).child(grp8,grp9,url)

# print(json.dumps(root.as_dict(), indent=4))
json_object=json.dumps(root.as_dict(),indent = 4) 
with open("data3.json", "w") as outfile:
    outfile.write(json_object)