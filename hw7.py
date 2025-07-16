vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def count_vowels(text):
    listletters = list(text)
    listvowels = [x for x in listletters if x in vowels]
    result = len(listvowels)
    return result


word = count_vowels("Aethoiyb")
print(word)


def count_words(sentence):
    wordslist = sentence.split()
    result = len(wordslist)
    return result


sen = count_words("Lorem ipsum dolor sit amet dolor sit lr")
print("Кількість слів в тексті:", sen)
