import random

# Визначаємо алфавіт
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Генеруємо список з 100 000 випадкових символів
random_text = ''.join(random.choices(alphabet, k=100000))

# Записуємо у файл
with open('random_text.txt', 'w') as file:
    file.write(random_text)

print("Текст згенеровано та збережено у файлі random_text.txt")