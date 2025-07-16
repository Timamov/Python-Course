question = input("Введіть текст:")
if type(question) is str:
    if len(question) >= 10:
        print("Цей текст довгий")
    elif len(question) <= 5:
        print("Цей текст короткий")
    elif len(question) > 5 and len(question) < 10:
        print("В самий раз")
else:
    print("Це не строка!!!!!!!!!!!!!😡")

condition1 = int(input("Введіть число 1:"))
condition2 = int(input("Введіть число 2:"))
operator = input("Введіть оператор:")
if operator == "додавання":
    print(condition1 + condition2)
elif operator == "віднімання":
    print(condition1 - condition2)
elif operator == "множення":
    print(condition1 * condition2)
elif operator == "ділення":
    if condition2 != 0:
        print(condition1 / condition2)
    else:
        print("На 0 не можна ділити!!!!!!!!")
else:
    print("Такого оператора не існує")
