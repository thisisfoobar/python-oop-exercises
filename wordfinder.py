from random import randint

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Find random words in a dictionary file:

    >>> word = WordFinder("words.txt")
    4 words read

    >>> word.random() in ["cat","dog","bird","squirrel"]
    True

    >>> word.random() in ["cat","dog","bird","squirrel"]
    True

    >>> word.random() in ["cat","dog","bird","squirrel"]
    True

    >>> word.random() in ["cat","dog","bird","squirrel"]
    True

    """
    def __init__(self,path):
        """initialize variables and show number of words in file"""
        self.path = path
        self.words = open(self.path,"r")
        self.wordlist = []
        self.wordsread()
        
    def __repr__(self):
        return f"<reading file {self.path} with {len(self.wordlist)} words"

    def wordsread(self):
        """opens and reads file"""
        for word in self.words:
            self.wordlist.append(word.strip())
        print(f"{len(self.wordlist)} words read")

    def random(self):
        """return random word from file"""
        randindx = randint(0,len(self.wordlist))
        return self.wordlist[randindx - 1]
        

class SpecialWordFinder(WordFinder):
    """Find random words in special word dictionary:
    >>> specialword = SpecialWordFinder("specialwords.txt")
    4 words read

    >>> specialword.random() in ["kale","parsnips","apple","mango"]
    True

    >>> specialword.random() in ["kale","parsnips","apple","mango"]
    True

    >>> specialword.random() in ["kale","parsnips","apple","mango"]
    True

    >>> specialword.random() in ["kale","parsnips","apple","mango"]
    True
    """
    def wordsread(self):
        """strip out words starting with # and blank lines"""
        for word in self.words:
            if not word.startswith("#") and word.strip():
                self.wordlist.append(word.strip())
        print(f"{len(self.wordlist)} words read")