from ordered_list import *
from huffman_bit_writer import *

class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.char!r})"

    def __eq__(self, other):
        if type(other) is not HuffmanNode:
            return False
        return self.freq == other.freq and self.char == other.char

    def __lt__(self, other):
        if self.freq == other.freq and self.char < other.char:
            return True
        if self.freq < other.freq:
            return True
        if self.freq > other.freq:
            return False
        return False

def cnt_freq(filename):
    f = open(filename, "r")
    chars = f.readline()
    freql = [0] * 256
    for c in chars:
        freql[ord(c)] += 1
    f.close()
    return freql

def create_huff_tree(list_of_freqs):
    sortedList = OrderedList()

    for i in range(len(list_of_freqs)):
        if list_of_freqs[i] != 0:
            sortedList.add(HuffmanNode(i, list_of_freqs[i]))

    if sortedList.size() == 0:
        return

    if sortedList.size() == 1:
        return sortedList.pop(0)

    while sortedList.size() > 1:
        first = sortedList.pop(0)
        second = sortedList.pop(0)

        if first.char < second.char:
            new_ascii = first.char
        else:
            new_ascii = second.char

        new_node = HuffmanNode(new_ascii, first.freq + second.freq)

        new_node.left = first
        new_node.right = second
        sortedList.add(new_node)

    # print(sortedList.python_list())
    return sortedList.head.next.item

def create_code(root_node):
    if root_node is None:
        return None
    l = [""] * 256
    huff_code = ""
    create_code_helper(root_node, l, huff_code)
    return l

def create_code_helper(node, l, huff_code):
    # print(node.left)
    if node.left is None and node.right is None:
        l[node.char] = huff_code
    if node.left:
        create_code_helper(node.left, l, huff_code + "0")
    if node.right:
        create_code_helper(node.right, l, huff_code + "1")

def huffman_encode(in_file, out_file):
    try:
        with open(in_file) as f:
            f.close()
    except FileNotFoundError:
        raise FileNotFoundError

    open_file = open(in_file, "r")
    read_file = open_file.read()
    open_file.close()

    empty = False
    if read_file == "":
        empty = True
        print("Input is empty, producing empty file")

    freq_list = cnt_freq(in_file)
    out_header = create_header(freq_list)
    huff_tree = create_huff_tree(freq_list)
    huff_code_list = create_code(huff_tree)
    huff_code = ""

    with open(in_file) as f:
        f_str = f.readlines()
        for line in f_str:
            for c in line:
                huff_code += huff_code_list[ord(c)]

    with open(out_file, "w") as f:
        if not empty:
            f.write(out_header + "\n")
        if len(out_header.split()) != 2:
            f.write(huff_code)

    compressed = out_file[0:len(out_file) - 4] + "_compressed.txt"
    comp = HuffmanBitWriter(compressed)
    if not empty:
        comp.write_str(out_header + "\n")
    comp.write_code(huff_code)
    comp.close()

def create_header(list_of_freqs):
    output = ""
    single_letter = 0
    for i in list_of_freqs:
        if i != 0:
            single_letter += 1
    for i in range(len(list_of_freqs)):
        if single_letter == 1 and list_of_freqs[i] != 0:
            output += str(i) + " "
            output += str(list_of_freqs[i]) + "\n"
        elif list_of_freqs[i] != 0:
            output += str(i) + " "
            output += str(list_of_freqs[i]) + " "
    return output
