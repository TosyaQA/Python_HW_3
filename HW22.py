# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum(lst):
    s = 0
    for n in range(len(lst)):
        if n % 2 != 0:
            s += lst[n]
    print(f"Сумма равна: {s}")

lst = [2, 3, 5, 9, 3]
sum(lst)
lst = list(map(int, input("Введите числа через прбел:\n").split()))
sum(lst)