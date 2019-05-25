import unittest
import trie

class TestTrieSearchMethods(unittest.TestCase):
    #Test initialization
    root = trie.TrieNode('*')
    
    
    def test_empty_trie(self):
        root = trie.TrieNode('*')
        self.assertEqual( trie.find_autocomplete(root, ''), [])
        
    def test_add_name(self):
        root = trie.TrieNode('*')
        self.assertEqual( trie.find_autocomplete(root, 'WhatsApp Messenger'), [])
        trie.add(root, 'WhatsApp Messenger')
        self.assertEqual( trie.find_autocomplete(root, 'WhatsApp Messenger'), ['WhatsApp Messenger'])
        
    def test_no_duplicates(self):
        root = trie.TrieNode('*')
        self.assertEqual( trie.find_autocomplete(root, 'WhatsApp Messenger'), [])
        trie.add(root, 'WhatsApp Messenger')
        self.assertEqual( trie.find_autocomplete(root, 'WhatsApp Messenger'), ['WhatsApp Messenger'])
        trie.add(root, 'WhatsApp Messenger')
        self.assertEqual( trie.find_autocomplete(root, 'WhatsApp Messenger'), ['WhatsApp Messenger'])
        
    def test_find_prefix_single_only(self):
        root = trie.TrieNode('*')
        trie.add(root, 'WhatsApp Messenger')
        self.assertEqual( trie.find_prefix(root, 'WhatsApp Messenger'), (True, 1))
        
    def test_find_prefix_single_more(self):
        root = trie.TrieNode('*')
        trie.add(root, 'WhatsApp Messenger')
        trie.add(root, 'Facebook')
        trie.add(root, 'PayPal')
        self.assertEqual( trie.find_prefix(root, 'WhatsApp Messenger'), (True, 1))
        
    def test_find_prefix_multiple(self):
        root = trie.TrieNode('*')
        trie.add(root, 'WhatsApp Messenger')
        trie.add(root, 'Facebook')
        trie.add(root, 'Facebook Lite')
        self.assertEqual( trie.find_prefix(root, 'Face'), (True, 2))
        
        
if __name__ == '__main__':
    unittest.main()