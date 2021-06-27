from FamilyTree import FamilyTree
from Relationship import GetRelationship
import os
import sys

ADD_CHILD="ADD_CHILD"
GET_RELATIONSHIP="GET_RELATIONSHIP"


def read_initial_tree(dir=None):
    family = FamilyTree()
    if not dir:
        dir=os.getcwd()
    path=os.path.join(dir, 'family_tree.txt')
    file = open(path, 'r')
    for line in file.readlines():
        line = line.rstrip()
        words = line.split()
        try:
            func=getattr(family, words[0].lower())
            func(*words[1:])
        except Exception as e:
            print(e)
            raise Exception(f'Module has no attribute named {words[0].lower()}')
    return family


def read_input(family, file):
    try:
        file = open(os.path.abspath(file), 'r')
    except Exception:
        raise Exception('File not found')
    else:
        for line in file.readlines():
            line=line.rstrip()
            elements=line.split()
            if elements[0]==ADD_CHILD:
                result = family.add_child(*elements[1:])
                print(result)
            elif elements[0]==GET_RELATIONSHIP:
                GetRelationship().form_function(family, elements)
            else:
                raise Exception('Invalid operation type')

if __name__=="__main__":
    if len(sys.argv)!=2:
        raise Exception('Invalid parameters')
    else:
        family = read_initial_tree()
        read_input(family, sys.argv[1])