def min_max_elements():
    question = input('Введіть числа через пробіл')
    list_number = question.split()
    min_number = min(list_number)
    max_number = max(list_number)
    print(f'Найменше число: {min_number}, Найбільше число: {max_number}')


min_max_elements()


def sort_function():
    ask_num = input('Введіть числа через пробіл щоб сортувати їх: ')
    num_list = ask_num.split()
    num_list = [int(x) for x in num_list]
    return sorted(num_list)


nums = sort_function()
print(nums)


def extraordinary_elements():
    question = input('Введіть слова')
    word_list = question.split()
    uniques = []
    for word in word_list:
        if word_list.count(word) == 1:
            uniques.append(word)
    print(uniques)


extraordinary_elements()
