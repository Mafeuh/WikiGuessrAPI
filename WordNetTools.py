import nltk
from nltk.corpus import wordnet
from googletrans import Translator

nltk.download('wordnet')

def get_lexical_field(word):
    synonyms = []

    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())

    # Remove duplicates
    synonyms = list(set(synonyms))

    return synonyms


def translate_words(words: [str], target_lang='fr')-> [str]:
    translator = Translator()
    data = [str]
    for word in words:
        data.append(translator.translate(word, dest=target_lang))
    return data
