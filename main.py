from argparse import ArgumentParser
from flask import Flask, request
import csv
import trie
import json

root = trie.TrieNode('*')
app = Flask(__name__)


def load_data(root, filename):
    """
    Loads the data in the file specified in the filename on the trie root parameter
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

@app.route('/autocomplete', methods=["Post"])
def get_autocomplete():
    prefix = request.get_data()
    results = trie.find_autocomplete(root, prefix.decode("utf-8"))
    print (results) #TODO for debug only
    return json.dumps("No Data")

if __name__ == "__main__":
    args = read_input()
    
    root = load_data(root, args.filename)
        
    app.run(debug=True, host="127.0.0.1", port=8080, threaded=True)

    
