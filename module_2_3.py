my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # записываем в переменную my_list массив (список) значений
elements_list = len(my_list)  # подсчитываем количество элементов в массиве
i = 0  # заводим индекс первого элемента массива
while i < elements_list:  # запускаем цикл - пока индекс элемента массива меньше общего количества элементов в массив
    if my_list[i] > 0:  # проверяем каждый элемент массива на то что он больше 0
        print(my_list[i])  # выводим элемент если подходит под условие
        i += 1  # переходим к следующему элементу массива (к первоначальному индексу прибавляем 1)
        continue  # если элемент попал под условие, то продолжаем цикл
    if my_list[i] == 0:  # проверяем каждый элемент массива на то что он равен 0
        i += 1  # переходим к следующему элементу массива (к первоначальному индексу прибавляем 1) и не выводим в консоль по условию задачи
        continue  # если элемент попал под условие, то продолжаем цикл
    else:
        break  # если элемент не попал под первое условие, то прерываем цикл
