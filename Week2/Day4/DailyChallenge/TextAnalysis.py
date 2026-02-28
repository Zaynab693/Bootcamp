import string
import re

# Part I: Text class
class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        count = words.count(word)
        return count if count > 0 else None

    def most_common_word(self):
        words = self.text.split()
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        return max(freq, key=freq.get)

    def unique_words(self):
        return list(set(self.text.split()))

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return cls(content)

# Part II: TextModification class
class TextModification(Text):
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        self.text = self.text.translate(translator)
        return self.text

    def remove_stop_words(self):
        stop_words = {'a', 'an', 'the', 'is', 'in', 'it', 'and', 'or', 'of', 'to', 'with', 'on', 'for', 'at', 'by', 'from'}
        self.text = ' '.join([w for w in self.text.split() if w.lower() not in stop_words])
        return self.text

    def remove_special_characters(self):
        self.text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return self.text
