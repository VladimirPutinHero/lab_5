import random

N = int(input("Введите значение N: "))

arr = list(range(1, N+1))

del_index = random.randint(0, N-1)

randArr = arr[0:del_index] + arr[del_index+1:]
random.shuffle(randArr)


def findDel(arr, randArr):
    n = len(arr)
    return ()


res = sum(arr) - sum(randArr)
print("Исходный набор чисел:", arr)
print("Перемешанный набор чисел:", randArr)
print("Удалённое число:", res)
