class Anagram:
    def __init__(self,word):
        self.word =word.lower()

    def match(self,words):
        anagrams = []
        for word in words:
            if sorted(self.word) == sorted(word.lower()) and self.word != word.lower():
                anagrams.append(word)
        return anagrams