
'''
Написати функцію, іка буде рахувати факторіал
'''

# 5! = 5 * 4 * 3 * 2 * 1
# Як тільки число доходить до 0, ми зупиняємось

# 1) Створити змінну, в яку ми будемо записувати значення
# 2) Пройтися по числам від n до 1 (від 1 до n) [Як тільки число доходить до 0, ми зупиняємось]
# 3) Помножити змінну на це число
# 4) Повернути результат
def factorial_non_recursive(n: int) -> int: # 5
    result = 1 # Можна також почати з числа
    for number in range(2, n + 1):
        result *= number # result = result * number -= +=
    return result

# print(factorial_non_recursive(3))
# print(factorial_non_recursive(1))

# 5! = 5 * 4 * 3 * 2 * 1 = 120

# Формула рекурсії:
# 1) Задати функцію
# 2.1) Написати умову, за якою зупиняється наша рекурсія
# 2.2) Якщо умова зупинки не виконується, ми йдемо далі (Рекурсивний крок)
# 3) Якщо дійшли до умови виходу, зупиняємось і повертаємо кінцеве значення

def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)

# print(factorial(3))
# print(factorial(1))

def factorial_explained(n: int, level=0) -> int:
    if n == 1:
        print(f'Level: {level} - factorial(1) = 1')
        return 1
    print(f'Level: {level} - factorial({n}) = {n} * factorial({n - 1})')
    result = n * factorial_explained(n - 1, level + 1)
    print(f'Level: {level} - factorial({n}) = {result}')
    return result

print(factorial_explained(5))
