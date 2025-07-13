numList = [x ** 2 for x in range(1, 6)]
print(numList)

question = input('Введіть слова через пробіл')
wordList = question.split()
index = 0
count = 0
for word in wordList:
    count = wordList.count(wordList[index])
    index += 1
    print(count)

# бібліотекою
