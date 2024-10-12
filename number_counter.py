from collections import Counter
"""
В нас є список з чисел, потрібно написати функцію, яка буде рахувати кількість повторень чисел
"""

numbers = [5, 0, 1, 2, 1, 1, 2, 2, 3, 5, 0]

# 1) Пройтися по усім числам у списку
# 2.1) Якщо число ще не зустрічалось, потрібно йому задати значення 1
# 2.2) Якщо число вже зустрічалось, потрібно взяти попередне значення і збільшити його на 1
# 3) Зберегти цю інформацію
# 4) Повернути значення
# 
# {5: 2, 0: 2, 1: 3} 
# five_count = 2
# one_count = 3

def count_numbers_in_a_list(numbers_list: list[int]) -> dict:
    counted_numbers = dict()
    for number in numbers_list:
        if number in counted_numbers: # 1 {1: 2} -> True
            counted_numbers[number] += 1
        else:
            counted_numbers[number] = 1
    return counted_numbers

def count_numbers_in_a_list_alternative(numbers_list: list[int]) -> dict:
    return Counter(numbers_list)


result_dict = count_numbers_in_a_list_alternative(numbers)
print(result_dict.most_common(1))
