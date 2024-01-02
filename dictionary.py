words = set()#here I have an equivalent of a hash table


def check(word): #implements hash table
    if word.lower() in words:
        return True
    else:
        return False

def load(dictionary):
    file = open(dictionary, "r")
    for line in file: 
        word = line.rstrip()
        words.add(line)
    file.close()
    return True


def size():
    return len(words)

def unload():
    return True