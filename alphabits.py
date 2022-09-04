
from typing import Optional, List


class HuffmanNode:
    
    def __init__(self, char: str, count: int, l_ref: Optional["HuffmanNode"],
                 r_ref: Optional["HuffmanNode"]) -> None:
        self.char = char
        self.count = count
        self.l_ref = l_ref
        self.r_ref = r_ref

    def __eq__(self, other: Optional["HuffmanNode"]) -> bool:
        if other is None:
            return False
        return (self.char == other.char and self.count == other.count
                and self.l_ref == other.l_ref and self.r_ref == other.r_ref)

    def __repr__(self) -> str:
        s = f"{self.char}:{self.count}"
        if self.l_ref is not None:
            s += " " + str(self.l_ref)
        if self.r_ref is not None:
            s += " " + str(self.r_ref)
        return s


#CREATE TREES


def create_tree(chars: str) -> Optional[HuffmanNode]:
    if len(chars) == 0:
        return None
    if len(chars) == 1:
        tree = HuffmanNode(chars, 1, None, None)
        return tree
    frequency_list = count_frequency(chars, ascii_count=[])
    trees = convert_into_nodes(frequency_list, new=[])
    trees = sort_trees(trees)
    print(trees)
    while len(trees) != 1:
        trees = tree_maker(trees)
        print(trees)
    return trees[0]

def count_frequency(chars: str, ascii_count: List[int]) -> List[int]:
    for i in range(256):
        ascii_count.append(0)
    for item in chars:
        ascii_number = ord(item)
        ascii_count[ascii_number] += 1
    return ascii_count

def convert_into_nodes(list: List[int], new: List[HuffmanNode]) -> List[HuffmanNode]:
    for i in range(256):
        if list[i] != 0:
            node = HuffmanNode(chr(i), list[i], None, None)
            new.append(node)
    return new

def sort_trees(trees: List[HuffmanNode]) -> List[HuffmanNode]:
    for item in trees:
        item.char = str(ord(item.char))
    for index in range(1, len(trees)):
        cur_val = int(trees[index].char)
        pos = index
        while pos > 0 and int(trees[pos - 1].char) > cur_val:
            hold = trees[pos]
            trees[pos] = trees[pos - 1]
            trees[pos - 1] = hold
            pos -= 1
            trees[pos].char = str(cur_val)
    for item in trees:
        item.char = chr(int(item.char))
    for index in range(1, len(trees)):
        cur_val = trees[index].count
        pos = index
        while pos > 0 and trees[pos - 1].count > cur_val:
            hold = trees[pos]
            trees[pos] = trees[pos - 1]
            trees[pos - 1] = hold
            pos -= 1
            trees[pos].count = cur_val
    return trees



def tree_maker(trees):
    parent_count = trees[0].count + trees[1].count
    if ord(trees[0].char) < ord(trees[1].char):
        parent_char = trees[0].char
    else:
        parent_char = trees[1].char
    lower = trees[0]
    higher = trees[1]
    if lower.count == higher.count:
        if ord(trees[0].char) > ord(trees[1].char):
            lower = trees[1]
            higher = trees[0]
    trees.pop(0)
    trees.pop(0)
    parent = HuffmanNode(parent_char, parent_count, lower, higher)
    trees.append(parent)
    trees = sort_trees(trees)
    return trees



#ENCODE




def encode(chars: str, root: Optional[HuffmanNode]) -> str:
    if root is None:
        return ''
    code = ''
    for char in chars:
        bits = find_letter_code(char, root, acc='')
        code += bits
    return code


def find_letter_code(char, root: Optional[HuffmanNode], acc) -> str:
    if root.l_ref is None and root.r_ref is None:
        if root.char == char:
            return acc
        else:
            return ''
    left = find_letter_code(char, root.l_ref, acc + '0')
    if left == '':
        return find_letter_code(char, root.r_ref, acc + '1')
    else:
        return left




#DECODE




def decode(bits: str, root: Optional[HuffmanNode]) -> str:
    if root is None:
        return ''
    phrase = ''
    while bits != ' ':
        answer = find_letter(bits, root, char='')
        bits = answer[0]
        phrase += answer[1]
    return phrase


def find_letter(bits: str, root: Optional[HuffmanNode], char: str) -> List[str]:
    index = 0
    if bits[-1] != ' ':
        bits += ' '
    for i in range(len(bits)):
        if bits[i] == '0':
            root = root.l_ref
        elif bits[i] == '1':
            root = root.r_ref
        if root.l_ref is None and root.r_ref is None:
            index = i
            char = root.char
            break
    leftover_bits = ''
    for k in range(len(bits)):
        if k > index:
            leftover_bits += bits[k]
    return [leftover_bits, char]



def main() -> None:
    chars = input("Treeify: ")  # initial chars used to create Huffman tree
    root = create_tree(chars)
    while True:
        try:
            chars = input(">>> ")  # chars to encode
            code = encode(chars, root)
            assert decode(code, root) == chars
            print(code)
        except AssertionError:
            print("Encode/Decode Failure")
        except EOFError:  # loop breaks with CTRL+d
            break
    print()


if __name__ == "__main__":
    main()
