from AVLT import AVLT
from AVLT import Node
from RBT import RedBlackTree
from RBT import RBTNode

#Going to read and insert the words into the tree
def pop_tree(txt_file, tree):
    file = open(txt_file, "r")
    for line in file:
        l = line.split("\n")
        #TODO red black and avl tree
        if isinstance(tree, AVLT):
                tree.insert(Node(l[0]))
        else:
                tree.insert(RBTNode(l[0]))

#Going to print the anagrams of the words and the count of the those anagram words
def anagram(tree, word, prefix = "", p = True):
        words = []
        def print_anagram(word, prefix):
                if len(word) <= 1:
                        str = prefix + word
                        n = tree.search(str)
                        if n is not None:
                                if p:
                                        print(n.key)
                                words.append(n.key)
                else:
                        for i in range(len(word)):
                                cur = word [i: i + 1]
                                before = word[0:i]
                                after = word[i +1:]
                                if cur not in before:
                                        print_anagram(before + after, prefix + cur)
        print_anagram(word, prefix)
        if p:
                print("Count: ", len(words))
        return words

#Going to find the greatest word with the most anagram in the file
def greatest_anagram(file):
        file = open(file, "r")
        max = 0
        word = ""
        for line in file:
                l = line.split("\n")
                n = anagram(tree, l[0], "", False)
                if max < len(n):
                        max = len(n)
                        word = n[0]
        #Going to print the word with the most angrams along with the numeber of angrams
        print(word,max)

global tree
# i = input("0)AVLT\n1)RBT\n")
# if i is "0":
#         print("Populating AVL tree...")
#         tree = AVLT()
# else:
print("Populating RB tree...")
tree = RedBlackTree()
pop_tree("words.txt", tree)
anagram(tree, "money")
print("Finding the word with the greatest number of anagrams")
greatest_anagram("words_example.txt")

