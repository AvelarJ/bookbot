import sys

from stats import get_num_words
from stats import get_num_char
from stats import formatCharDict

def main():    
    #file_path = "books/frankenstein.txt"
    try: 
        file_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n----------- Word Count ----------")
    
    wordCount = get_num_words(file_path)
    print(f"Found {wordCount} total words")
    
    print("--------- Character Count -------")
    
    charDict = get_num_char(file_path)
    orderedCharDict = formatCharDict(list(charDict.items()))
    
    for item in orderedCharDict:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
            
            
    print("============= END ===============")
    
main()