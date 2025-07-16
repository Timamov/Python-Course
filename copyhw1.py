memory = 5000
files = 20
fileGb = 256
filesInMemory = memory // fileGb
print(filesInMemory)
gbInMemory = filesInMemory * fileGb
print(gbInMemory)
extraFiles = memory - gbInMemory
print("Помістилось:", filesInMemory, "Залишилось:", extraFiles, "Gb")

question = int(input("Введіть градуси за фаренгейтом:"))

print(question)
actionFarenheit = question - 32
result = actionFarenheit * 5 // 9
print("Градусів цельсія:", result)

sum = int(input("Введіть суму покупки"))
percents = 7
print(sum)
cashback = sum / 100 * percents
print("Кєшбек:", cashback)
