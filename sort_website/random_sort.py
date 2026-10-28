import random

def is_sorted(a):
    return all(a[i] <= a[i+1] for i in range(len(a)-1))

def bogosort(a):
    a = a.copy()
    tries = 0
    # Защита от зависания сервера
    if len(a) > 9:
        return a, "Ошибка: для Bogo Sort введите не больше 9 чисел, иначе сервер зависнет!"
        
    while not is_sorted(a):
        random.shuffle(a)
        tries += 1
    return a, f"Попыток: {tries}"