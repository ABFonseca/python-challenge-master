from argparse import ArgumentParser
import csv
import trie



def load_data(root, filename):
    """
    Loads the data in the file specified in the filename on the trie passed on root parameter
    """
    try:
        with open(args.filename, 'r') as csv_file:
            for line in csv.reader(csv_file):
                trie.add(root, line[0])
        
        return root
    except (FileNotFoundError, IOError):
        print("Specified file does not exist or insuficient permissions")
        exit (2)

def read_input():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input_file", dest="filename",
            help="csv input file", metavar="FILE")
    args = parser.parse_args()
    
    if not args.filename or args.filename == '':
        parser.print_help()
        exit (1)
        
    return args


if __name__ == "__main__":
    args = read_input()
    
    root = load_data(trie.TrieNode('*'), args.filename)

    #TODO shold the search be case sensitive ?!
    print (trie.find_autocomplete(root, 'B'))
    print (trie.find_autocomplete(root, 'fac'))
    print (trie.find_autocomplete(root, 'Fac'))
    
