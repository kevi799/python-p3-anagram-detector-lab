# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, list_anagram):
        matches = []
        for word in list_anagram:

            if ''.join(sorted(word.lower())) == self.sorted_word and word.lower() != self.word:
                matches.append(word)
        return matches
    
pikachu = Anagram('listen')
words = ["enlists", "google", "inlets", "banana"]
print(pikachu.match(words))

