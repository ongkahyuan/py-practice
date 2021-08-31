import operator

class q3:

    def __init__(self):
        self.f = open("sample_article.txt", "r", encoding="utf-8")
        self.text = self.f.read()
        self.sents = [e + "." for e in self.text.split(".") if e]
        self.words = [w.replace(".", "").replace(",", "") for w in self.text.split(" ") if w]

    def find_freq(self):
        word_dict = {}
        for word in self.words:
            if word in word_dict:
                word_dict[word] +=1
            else:
                word_dict[word] = 1
        # return sorted(word_dict, key=word_dict.get, reverse=True)[:10]
        return dict(sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True))

if __name__ == "__main__":
    s = q3()
    print(s.find_freq())