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
        return word_dict

    def find_first(self,word):
        for sent in self.sents:
            if word in sent:
                return sent

    def find_last(self,word):
        for sent in self.sents[::-1]:
            if word in sent:
                return sent

    def generate_list(self):
        word_dict = self.find_freq()
        out = []
        for i in range(10):
            word = sorted(word_dict, key=word_dict.get, reverse=True)[i]
            freq = word_dict[word]
            first = self.find_first(word)
            last = self.find_last(word)
            compiled = {}
            compiled["keyword"] = word
            compiled["frequency"] = freq
            compiled["first_time"] = first
            compiled["last_time"] = last
            out.append(compiled)
        return out

if __name__ == "__main__":
    s = q3()
    print(s.generate_list())