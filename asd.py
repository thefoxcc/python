import re
import math

with open('input.txt', 'r') as file:
    data = file.read()
print('Содержимое файла:', data)

octal_numbers_pattern = r'\b5[0-7]*\b'
octal_numbers = re.findall(octal_numbers_pattern, data)
octal_numbers = [int(num, 8) for num in octal_numbers]
octal_sum = sum(octal_numbers)
octal_product = math.prod(octal_numbers) if octal_numbers else 1

print('Найденные восьмеричные числа:', octal_numbers)
print('Сумма чисел:', octal_sum)
print('Произведение чисел:', octal_product)