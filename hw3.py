name = input("Type your name:")
middleName = input("Type your middle-name")

initial = name[0] + "." + middleName[0]
print("Ваш ініціал:", initial.upper())

word = input("Type a word:").lower()
palindrome = word[::-1]
if word == palindrome:
    print("It's palidrome")
else:
    print("It's not palidrome")

firstWord = input("Type the first word:")
secWord = input("Type the second word:")
thirdWord = input("Type the third word")

if len(firstWord) > len(secWord) and len(firstWord) > len(thirdWord):
    print(f"Найдовше слово: {firstWord}")
elif len(secWord) > len(firstWord) and len(secWord) > len(thirdWord):
    print(f"Найдовше слово: {secWord}")
if len(thirdWord) > len(firstWord) and len(thirdWord) > len(secWord):
    print(f"Найдовше слово: {thirdWord}")
