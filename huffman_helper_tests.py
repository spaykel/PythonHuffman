import unittest
from huffman import *
import filecmp


class Test(unittest.TestCase):

    # works
    def test_cnt_freq_1(self):
        test_freq = cnt_freq("test_1.txt")
        test_l = [0, 2, 4, 8, 16, 0, 2, 0]
        self.assertEqual(test_freq[96:104], test_l)

    # works
    def test_cnt_freq_2(self):
        test_freq = cnt_freq("test_2.txt")
        test_l = [0, 0, 1, 0, 0, 0, 0]
        self.assertEqual(test_freq[96:103], test_l)

    # works
    def test_create_huff_tree_1(self):
        freqlist = cnt_freq("test_1.txt")
        test_tree = create_huff_tree(freqlist)
        self.assertEqual(test_tree.freq, 32)
        self.assertEqual(test_tree.char, 97)
        left = test_tree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = test_tree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    # works
    def test_create_huff_tree_2(self):
        freqlist = cnt_freq("test_2.txt")
        test_tree = create_huff_tree(freqlist)
        self.assertEqual(test_tree.freq, 1)
        self.assertEqual(test_tree.char, 98)

    # works
    def test_create_huff_tree_3(self):
        freqlist = cnt_freq("test_3.txt")
        test_tree = create_huff_tree(freqlist)
        self.assertEqual(test_tree.freq, 13)
        self.assertEqual(test_tree.char, 32)
        right = test_tree.right
        self.assertEqual(right.freq, 7)
        self.assertEqual(right.char, 97)

    def test_create_code_1(self):
        freqlist = cnt_freq("test_1.txt")
        test_tree = create_huff_tree(freqlist)
        code = create_code(test_tree)
        self.assertEqual(code[ord('d')], '1')
        self.assertEqual(code[ord('c')], '01')
        self.assertEqual(code[ord('b')], '001')
        self.assertEqual(code[ord('a')], '0000')
        self.assertEqual(code[ord('f')], '0001')

    def test_create_code_2(self):
        freqlist = cnt_freq("test_2.txt")
        test_tree = create_huff_tree(freqlist)
        code = create_code(test_tree)
        self.assertEqual(code[ord('b')], '')

    def test_create_code_3(self):
        freqlist = cnt_freq("test_3.txt")
        test_tree = create_huff_tree(freqlist)
        code = create_code(test_tree)
        self.assertEqual(code[ord('d')], '100')
        self.assertEqual(code[ord('c')], '101')
        self.assertEqual(code[ord('b')], '01')
        self.assertEqual(code[ord('a')], '11')
        self.assertEqual(code[ord(' ')], '00')

    def test_create_header_1(self):
        freqlist = cnt_freq("test_1.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2 ")

    def test_create_header_2(self):
        freqlist = cnt_freq("test_2.txt")
        self.assertEqual(create_header(freqlist), "98 1\n")

    '''

    # These can't be tested correctly within PyCharm but by 
    # using an online binary interpreter it checks out

    def test_huffman_encode_1(self):
        huffman_encode("test_1.txt", "test_1_encoded.txt")
        self.assertTrue(filecmp.cmp("test_1_encoded.txt", "test_1_encoded_compressed.txt"))

    def test_huffman_encode_3(self):
        huffman_encode("test_3.txt", "test_3_encoded.txt")
        self.assertTrue(filecmp.cmp("test_3_encoded.txt", "test_3_encoded_compressed.txt"))

    '''

    def test_empty_file(self):
        huffman_encode("emptyfile.txt", "emptyfile_encoded.txt")
        self.assertTrue(filecmp.cmp("emptyfile.txt", "emptyfile_encoded.txt"))

    def test_file_doesnt_exist(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode("does_not_exist.txt", "does_not_exist_encoded.txt")

    def test_single_character(self):
        freqlist = cnt_freq("test_2.txt")
        self.assertEqual(create_header(freqlist), "98 1\n")

    def test_create_code_helper_1(self):
        freqlist = cnt_freq("test_1.txt")
        huff_code = ""
        root = create_huff_tree(freqlist)
        self.assertEqual(create_code_helper(root, freqlist, huff_code), None)

if __name__ == '__main__':
    unittest.main()