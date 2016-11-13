import enchant

class Spellcheck:
    def __init__(self, words):
        self.dictionary = enchant.request_pwl_dict("/dev/null")
        for w in words:
            self.dictionary.add_to_pwl(w)

    def check(self, word):
        if self.dictionary.check(word):
            return word
        else:
            suggestions = self.dictionary.suggest(word)

            if suggestions and len(suggestions) > 0:
                return suggestions[0]
            else:
                return word
