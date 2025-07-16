question = input("Введіть назву місяця або його число:")
if question == "January" or question == "1":
    print("Зараз зима")
elif question == "February" or question == "2":
    print("Зараз зима")
elif question == "December" or question == "12":
    print("Зараз зима")

elif question == "March" or question == "3":
    print("Зараз весна")
elif question == "April" or question == "4":
    print("Зараз весна")
elif question == "May" or question == "5":
    print("Зараз весна")

elif question == "June" or question == "6":
    print("Зараз літо")
elif question == "July" or question == "7":
    print("Зараз літо")
elif question == "August" or question == "8":
    print("Зараз літо")

elif question == "September" or question == "9":
    print("Зараз осінь")
elif question == "October" or question == "10":
    print("Зараз ocінь")
elif question == "November" or question == "11":
    print("Зараз осінь")
else:
    print("Це не місяць!")

questionPrice = int(input("Введіть суму покупки:"))
questionTime = int(input("Введіть час, коли покупка була здійснена"))
if 20 <= questionTime <= 22:
    print("Разом до сплати:", questionPrice / 2)
elif 8 <= questionTime <= 19:
    print("Разом до сплати:", questionPrice)
else:
    print("Зараз магазин не працює")
