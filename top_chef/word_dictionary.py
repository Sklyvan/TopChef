class WordDictionaryException(Exception):
    pass

class WordDictionary:

    def __init__(self):
        self.words = {}

    def load_words(self, word_path):
        try:
            wordsFile = open(word_path,"r")
            wordsList = []
            for word in wordsFile:
                if "WORD" not in word:
                    wordsList.append(word)

            wordsFile.close()

            for word in wordsList:
                aux = word.replace("\n", "")
                aux = aux.split("\t")
                key = aux[0]
                value = float(aux[1])
                self.words[key] = value
        except:
            raise WordDictionaryException ("Wrong data file.")

    def add_word(self, word, value):
        self.words[word] = value

    def exists(self, word):
        return word in self.words

    def get_value(self, word):
        return self.words[word]

    def get_words(self):
        return self.words.keys()

    def __str__(self):
        word_str = ""
        for word in self.words:
            word_str += word + ": " + str(self.words[word]) + "\n"
        return word_str

    def __len__(self):
        return len(self.words)