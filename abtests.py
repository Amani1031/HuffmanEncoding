# Name:         Amani Arora
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   AlphaBits
# Term:         Spring 2021

import unittest

import alphabits
from alphabits import HuffmanNode as H  # only allowed use of from ... import


class TestCreateTree(unittest.TestCase):

    def test_create_tree_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.create_tree("DEADBEEFCAFE"), root)

    def test_create_tree_2(self):
        root = H("A", 13, H("E", 5, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.create_tree("DEADBEEFCAFEE"), root)

    def test_create_tree_3(self):
        root = H("A", 14, H("E", 6, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.create_tree("DEADBEEFCAFEEE"), root)

    def test_create_tree_4(self):
        root = H("A", 15, H("E", 7, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.create_tree("DEADBEEFCAFEEEE"), root)

    def test_create_tree_5(self):
        root = H("D", 1, None, None)
        self.assertEqual(alphabits.create_tree("D"), root)


class TestCountFrequency(unittest.TestCase):

    def test_count_frequency_1(self):
        lst = []
        count = 0
        while count < 256:
            lst.append(0)
            count += 1
        lst[65] = 2
        lst[66] = 1
        lst[67] = 1
        lst[68] = 2
        lst[69] = 4
        lst[70] = 2
        self.assertEqual(alphabits.count_frequency("DEADBEEFCAFE", ascii_count=[]), lst)

    def test_count_frequency_2(self):
        lst = []
        count = 0
        while count < 256:
            lst.append(0)
            count += 1
        lst[104] = 1
        lst[101] = 1
        lst[108] = 2
        lst[111] = 1
        self.assertEqual(alphabits.count_frequency("hello", ascii_count=[]), lst)

    def test_count_frequency_3(self):
        lst = []
        count = 0
        while count < 256:
            lst.append(0)
            count += 1
        lst[68] = 2
        lst[65] = 1
        lst[78] = 2
        lst[69] = 1
        lst[76] = 1
        lst[73] = 1
        lst[79] = 1
        lst[33] = 1
        self.assertEqual(alphabits.count_frequency("DANDELION!", ascii_count=[]), lst)

    def test_count_frequency_4(self):
        lst = []
        count = 0
        while count < 256:
            lst.append(0)
            count += 1
        lst[78] = 1
        lst[79] = 1
        lst[77] = 1
        lst[87] = 1
        lst[72] = 1
        lst[69] = 3
        lst[82] = 1
        lst[64] = 1
        self.assertEqual(alphabits.count_frequency("NOWHERE@ME", ascii_count=[]), lst)

    def test_count_frequency_5(self):
        lst = []
        count = 0
        while count < 256:
            lst.append(0)
            count += 1
        lst[65] = 1
        self.assertEqual(alphabits.count_frequency("A", ascii_count=[]), lst)

#yet to do
class TestConvertIntoNodes(unittest.TestCase):

    def test_convert_into_nodes_1(self):
        frequency = alphabits.count_frequency("DEADBEEFCAFE", ascii_count=[])
        nodes = [H('A', 2, None, None), H('B', 1, None, None),
                 H('C', 1, None, None), H('D', 2, None, None),
                 H('E', 4, None, None), H('F', 2, None, None)]
        self.assertEqual(alphabits.convert_into_nodes(frequency, new=[]), nodes)

    def test_convert_into_nodes_2(self):
        frequency = alphabits.count_frequency("DEADBEEFCAFEE", ascii_count=[])
        nodes = [H('A', 2, None, None), H('B', 1, None, None),
                 H('C', 1, None, None), H('D', 2, None, None),
                 H('E', 5, None, None), H('F', 2, None, None)]
        self.assertEqual(alphabits.convert_into_nodes(frequency, new=[]), nodes)

    def test_convert_into_nodes_3(self):
        frequency = alphabits.count_frequency("DEADBEEFCAFEEE", ascii_count=[])
        nodes = [H('A', 2, None, None), H('B', 1, None, None),
                 H('C', 1, None, None), H('D', 2, None, None),
                 H('E', 6, None, None), H('F', 2, None, None)]
        self.assertEqual(alphabits.convert_into_nodes(frequency, new=[]), nodes)

    def test_convert_into_nodes_4(self):
        frequency = alphabits.count_frequency("DEADBEEFCAFEEEE", ascii_count=[])
        nodes = [H('A', 2, None, None), H('B', 1, None, None),
                 H('C', 1, None, None), H('D', 2, None, None),
                 H('E', 7, None, None), H('F', 2, None, None)]
        self.assertEqual(alphabits.convert_into_nodes(frequency, new=[]), nodes)

    def test_convert_into_nodes_5(self):
        frequency = alphabits.count_frequency("DEADBEEFCAFEEEEE", ascii_count=[])
        nodes = [H('A', 2, None, None), H('B', 1, None, None),
                 H('C', 1, None, None), H('D', 2, None, None),
                 H('E', 8, None, None), H('F', 2, None, None)]
        self.assertEqual(alphabits.convert_into_nodes(frequency, new=[]), nodes)

class TestSortTrees(unittest.TestCase):

    def test_sort_trees_1(self):
        nodes = [H('A', 2, None, None), H('B', 1, None, None),
                 H('C', 1, None, None), H('D', 2, None, None),
                 H('E', 4, None, None), H('F', 2, None, None)]
        sorted =[H('B', 1, None, None), H('C', 1, None, None),
                 H('A', 2, None, None), H('D', 2, None, None),
                 H('F', 2, None, None), H('E', 4, None, None)]
        self.assertEqual(alphabits.sort_trees(nodes), sorted)

    def test_sort_trees_2(self):
        nodes = [H('A', 2, None, None), H('B', 1, None, None),
                 H('C', 1, None, None), H('D', 2, None, None),
                 H('E', 6, None, None), H('F', 2, None, None)]
        sorted =[H('B', 1, None, None), H('C', 1, None, None),
                 H('A', 2, None, None), H('D', 2, None, None),
                 H('F', 2, None, None), H('E', 6, None, None)]
        self.assertEqual(alphabits.sort_trees(nodes), sorted)

    def test_sort_trees_3(self):
        nodes = [H('A', 2, None, None), H('B', 1, None, None),
                 H('C', 1, None, None), H('D', 2, None, None),
                 H('E', 9, None, None), H('F', 2, None, None)]
        sorted =[H('B', 1, None, None), H('C', 1, None, None),
                 H('A', 2, None, None), H('D', 2, None, None),
                 H('F', 2, None, None), H('E', 9, None, None)]
        self.assertEqual(alphabits.sort_trees(nodes), sorted)

    def test_sort_trees_4(self):
        nodes = [H('A', 2, None, None), H('B', 1, None, None),
                 H('C', 1, None, None), H('D', 2, None, None),
                 H('E', 7, None, None), H('F', 2, None, None)]
        sorted =[H('B', 1, None, None), H('C', 1, None, None),
                 H('A', 2, None, None), H('D', 2, None, None),
                 H('F', 2, None, None), H('E', 7, None, None)]
        self.assertEqual(alphabits.sort_trees(nodes), sorted)

    def test_sort_trees_5(self):
        nodes = [H('A', 2, None, None), H('B', 1, None, None),
                 H('C', 1, None, None), H('D', 2, None, None),
                 H('E', 11, None, None), H('F', 2, None, None)]
        sorted =[H('B', 1, None, None), H('C', 1, None, None),
                 H('A', 2, None, None), H('D', 2, None, None),
                 H('F', 2, None, None), H('E', 11, None, None)]
        self.assertEqual(alphabits.sort_trees(nodes), sorted)

class TestTreeMaker(unittest.TestCase):

    def test_tree_maker_1(self):
        nodes = [H('B', 1, None, None), H('C', 1, None, None),
                 H('A', 2, None, None), H('D', 2, None, None),
                 H('F', 2, None, None), H('E', 4, None, None)]
        result = [H('A', 2, None, None),
                H('B', 2, H('B', 1, None, None), H('C', 1, None, None)),
                 H('D', 2, None, None), H('F', 2, None, None),
                 H('E', 4, None, None)]
        self.assertEqual(alphabits.tree_maker(nodes), result)

    def test_tree_maker_2(self):
        nodes = [H('B', 1, None, None), H('C', 1, None, None),
                 H('A', 2, None, None), H('D', 2, None, None),
                 H('F', 2, None, None), H('E', 5, None, None)]
        result = [H('A', 2, None, None),
                H('B', 2, H('B', 1, None, None), H('C', 1, None, None)),
                 H('D', 2, None, None), H('F', 2, None, None),
                 H('E', 5, None, None)]
        self.assertEqual(alphabits.tree_maker(nodes), result)

    def test_tree_maker_3(self):
        nodes = [H('B', 1, None, None), H('C', 1, None, None),
                 H('A', 2, None, None), H('D', 2, None, None),
                 H('F', 2, None, None), H('E', 6, None, None)]
        result = [H('A', 2, None, None),
                H('B', 2, H('B', 1, None, None), H('C', 1, None, None)),
                 H('D', 2, None, None), H('F', 2, None, None),
                 H('E', 6, None, None)]
        self.assertEqual(alphabits.tree_maker(nodes), result)

    def test_tree_maker_4(self):
        nodes = [H('B', 1, None, None), H('C', 1, None, None),
                 H('A', 2, None, None), H('D', 2, None, None),
                 H('F', 2, None, None), H('E', 7, None, None)]
        result = [H('A', 2, None, None),
                H('B', 2, H('B', 1, None, None), H('C', 1, None, None)),
                 H('D', 2, None, None), H('F', 2, None, None),
                 H('E', 7, None, None)]
        self.assertEqual(alphabits.tree_maker(nodes), result)

    def test_tree_maker_5(self):
        nodes = [H('B', 1, None, None), H('C', 1, None, None),
                 H('A', 2, None, None), H('D', 2, None, None),
                 H('F', 2, None, None), H('E', 8, None, None)]
        result = [H('A', 2, None, None),
                H('B', 2, H('B', 1, None, None), H('C', 1, None, None)),
                 H('D', 2, None, None), H('F', 2, None, None),
                 H('E', 8, None, None)]
        self.assertEqual(alphabits.tree_maker(nodes), result)


class TestEncode(unittest.TestCase):

    def test_encode_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("BE", root), "10100")

    def test_encode_2(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("AFAC", root), "1001111001011")

    def test_encode_3(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("BH", root), "10100")

    def test_encode_4(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("BG", root), "10100")

    def test_encode_5(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("BQ", root), "10100")

class TestFindLetterCode(unittest.TestCase):

    def test_find_letter_code_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("B", root), "1010")

    def test_find_letter_code_2(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("F", root), "111")

    def test_find_letter_code_3(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("E", root), "0")

    def test_find_letter_code_4(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("A", root), "100")

    def test_find_letter_code_5(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.encode("C", root), "1011")




class TestDecode(unittest.TestCase):

    def test_decode_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("10100", root), "BE")

    def test_decode_2(self):
        root = H("A", 12, H("E", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("1001111001011", root), "AFAC")

    def test_decode_3(self):
        root = H("A", 12, H("U", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("10100", root), "BU")

    def test_decode_4(self):
        root = H("A", 12, H("W", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("10100", root), "BW")

    def test_decode_5(self):
        root = H("A", 12, H("L", 4, None, None),
                 H("A", 8, H("A", 4, H("A", 2, None, None),
                             H("B", 2, H("B", 1, None, None),
                               H("C", 1, None, None))),
                   H("D", 4, H("D", 2, None, None),
                     H("F", 2, None, None))))
        self.assertEqual(alphabits.decode("10100", root), "BL")

class TestFindLetter(unittest.TestCase):

    def test_find_letter_1(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        answer = [' ', 'E']
        self.assertEqual(alphabits.find_letter("0", root, char=''), answer)

    def test_find_letter_2(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        answer = [' ', 'B']
        self.assertEqual(alphabits.find_letter("1010", root, char=''), answer)

    def test_find_letter_3(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        answer = ['100 ', 'B']
        self.assertEqual(alphabits.find_letter("1010100", root, char=''), answer)

    def test_find_letter_4(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        answer = [' ', 'A']
        self.assertEqual(alphabits.find_letter("100", root, char=''), answer)

    def test_find_letter_5(self):
        root = H("A", 12, H("E", 4, None, None),
                          H("A", 8, H("A", 4, H("A", 2, None, None),
                                              H("B", 2, H("B", 1, None, None),
                                                        H("C", 1, None, None))),
                                    H("D", 4, H("D", 2, None, None),
                                              H("F", 2, None, None))))
        answer = [' ', 'F']
        self.assertEqual(alphabits.find_letter("111", root, char=''), answer)


if __name__ == "__main__":
    unittest.main()
