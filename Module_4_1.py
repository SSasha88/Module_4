from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(69, 3)

result2 = fake_divide(3, 0)

result3 = true_divide(49, 7)

result4 = true_divide(15, 0)

# Результаты:
print('Домашняя работа по уроку "Модули и пакеты"')
print()
print("Результат деления через fake_math:", result1)
print("Результат деления через fake_math:", result2)
print("Результат деления через true_math:", result3)
print("Результат деления через true_math:", result4)