"""
Тема: tuple
"""
# ЗАДАНИЕ 1: Работа с кортежами
# Дано:
# coordinates = (10, 20, 30, 20, 10, 20, 40)
# 1. Выведите первый элемент кортежа
# 2. Выведите последний элемент кортежа
# 3. Выведите срез с 2-го по 4-й элемент (включительно)
# 4. Проверьте, есть ли число 30 в кортеже (используйте оператор in)
# 5. Найдите индекс первого вхождения числа 20
# 6. Подсчитайте, сколько раз встречается число 20
# 7. Подсчитайте, сколько раз встречается число 50 (его нет в кортеже)
# 8. Выведите длину кортежа

coordinates = (10, 20, 30, 20, 10, 20, 40)
print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:4])
if 30 in coordinates:
    print("Число 30 найдено")
print(coordinates.index(20))
print(coordinates.count(20))
print(coordinates.count(50))
print(len(coordinates))

# ЗАДАНИЕ 2: Операции с кортежами
# Дано:
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# numbers = [10, 20, 30, 40, 50]
# 1. Объедините tuple1 и tuple2 в один кортеж
# 2. Создайте кортеж, где элементы tuple1 повторяются 3 раза
# 3. Распакуйте tuple1 в три переменные a, b, c
# 4. Распакуйте numbers (преобразовав в кортеж) так, чтобы:
#    - первый элемент был в переменной first
#    - последний элемент был в переменной last
#    - все средние элементы были в списке middle
# 5. Преобразуйте список numbers в кортеж
# 6. Создайте кортеж из четных чисел от 0 до 10 (используйте генератор)
# 7. Создайте кортеж квадратов чисел от 1 до 5 (используйте генератор)
# 8. Создайте кортеж из одного элемента со значением 42

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
numbers = [10, 20, 30, 40, 50]
tuple3 = tuple1 + tuple2
print(tuple3)
new_tuple = tuple1 * 3
print(new_tuple)
a, b, c = tuple1
print(a, b, c)

numbers_tuple = tuple(numbers)
print(numbers_tuple)
first, *middle, last = numbers_tuple
print(numbers_tuple)
print("first =", first)
print("middle =", middle)
print("last: =", last)

numbers_as_tuple = tuple(numbers)
print("numbers кортеж:", numbers_as_tuple)

even_tuple = tuple(x for x in range(0, 11, 2))
print("Кортеж чётных чисел:", even_tuple)

squares_tuple = tuple(x**2 for x in range(1, 6))
print("Кортеж квадратов:", squares_tuple)

single_element_tuple = (42,)
print("Кортеж из одного элемента:", single_element_tuple)
