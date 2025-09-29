def sort_on(items):
    return items["num"]

def get_num_words(filePath):
    with open(filePath) as f:
        return len(f.read().split())
    
def get_num_char(filePath):
    charDict = {}
    with open(filePath) as f:
        for i in f.read():
            charDict[i.lower()] = charDict.get(i.lower(), 0) + 1
    return charDict

def formatCharDict(charDict):
    for key in charDict:
        charDict[charDict.index((key[0], key[1]))] = {"char": key[0], "num": key[1]}
    
    charDict.sort(reverse=True, key=sort_on)
    return charDict
