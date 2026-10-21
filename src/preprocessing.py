import re

# Имена файлов (исходный и очищенный)
input_file = "Harry_Potter_all.txt"
output_file = "Harry_Potter_cleaned.txt"

print(f"Чтение {input_file}...")
with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Приведение к нижнему регистру
text = text.lower()

# Оставляем только русские буквы и пробелы
text = re.sub(r'[^а-яё\s]+', ' ', text)

# Разбиваем на слова
words = text.split()

# Убираем слова короче 3 символов
words = [word for word in words if len(word) > 2]

print(f"Сохранение в {output_file}...")
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(' '.join(words))

print("Готово!")