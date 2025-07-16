numbers = []
while 0 not in numbers:
    question = int(input("Введіть число"))
    numbers.append(question)
    if 0 in numbers:
        quantity = len(numbers)
        increase = sum(numbers)
        arithmeticMea = increase / quantity
        print(
            f"Кількість чисел, які ви вводили: {quantity}, Сума цих чисел: {increase}, Середнє арифметичне: {arithmeticMea}"
        )

que = input("введіть текст")
countUpper = 0
countLower = 0
countDigit = 0
length = 0
for letter in que:
    if letter.isupper():
        countUpper += 1
    elif letter.islower():
        countLower += 1
    elif letter.isdigit():
        countDigit += 1
print(
    f"Кількість Великих літер {countUpper}, Кількість маленьких літер {countLower}, Кількість цифр {countDigit}"
)

crat = []
for number in range(100, 0, -1):
    if number % 5 == 0:
        crat.append(number)

print(sum(crat))
