import unittest
import trie
import csv

class TestTrieSearchMethods(unittest.TestCase):
    #Test initialization
    root = trie.TrieNode('*')
    with open('test_files/190titles.csv', 'r') as csv_file:
            for line in csv.reader(csv_file):
                trie.add(root, line[0])

    def test_not_found(self):
        self.assertEqual( trie.find_autocomplete(self.root, 'ABCD1234'), [])
    def test_exact_match(self):
        self.assertEqual( trie.find_autocomplete(self.root, 'WhatsApp Messenger'), ['WhatsApp Messenger'])
    def test_unique_match(self):
        self.assertEqual( trie.find_autocomplete(self.root, 'What'), ['WhatsApp Messenger'])
    def test_multiple_match(self):
        self.assertEqual( len(trie.find_autocomplete(self.root, 'W')), 4)
    def test_space_on_prefix(self):
        self.assertEqual( trie.find_autocomplete(self.root, 'Facebook L'), ['Facebook Lite'])
        
        
if __name__ == '__main__':
    unittest.main()