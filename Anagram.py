from AVLT import AVLT
from Node import Node

def pop_tree(txt_file, tree):
    file = open(txt_file, "r")
    for line in file:
        l = line.split("\n")
        tree.insert(Node(l[0]))

tree = AVLT()
pop_tree("words.txt", tree)
