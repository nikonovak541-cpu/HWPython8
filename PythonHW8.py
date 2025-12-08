# Подсчёт строк
# Посчитай и выведи количество строк в файле data.txt.

# file_path = ".\\.\\Python\\text.txt"
# stream = open(file_path, mode="r", encoding='utf-8')
# text = stream.readlines()
# stream.close()
# print(text)
# line_count = len(text)
# print(f"Количество строк в файле '{file_path}'): {line_count}")


# Задача 2
# Самая длинная строка
# Найди и выведи самую длинную строку в файле lines.txt (если несколько - выведи любую).
# file_path = ".\\.\\Python\\text.txt"
# stream = open(file_path, mode="r", encoding='utf-8')
# text = stream.readlines()
# stream.close()
# print(text)
# line_count = len(text)
# print(f"Количество строк в файле '{file_path}'): {line_count}")
# line = max(text, key=len)
# print(f"Самая длинная строка {len(line)}")


# Задача 3
# Поиск слова
# Попроси пользователя ввести слово. Посчитай и выведи, сколько раз это слово встречается в файле text.txt (регистр не учитывать).
# import string
# file_path = ".\\.\\Python\\text.txt"
# stream = open(file_path, mode="r", encoding='utf-8')
# text = stream.read()
# stream.close()
# print(text)
# line_count = len(text)
# print(f"Количество строк в файле '{file_path}'): {line_count}")
# line = max(text, key=len)
# print(f"Самая длинная строка {len(line)}")


# search_word = input("Введите слово для поиска: ")
# print(text.lower().count(search_word))

# if search_word:
#     print(f"Слово '{search_word}'")


# Задача 4
# Замена текста
# Прочитай файл old.txt. Замени все вхождения слова плохо на хорошо (регистр не учитывать) и запиши результат в файл new.txt.
# import re

# old_file_path = "old.txt"
# new_file_path = "new.txt"

# try:
#     with open (old_file_path, "w", encoding = 'utf-8') as f:
#         f.write("Плохо то что хорошо. Когда плохо, не всегда плохо. Однако, когда хорошо, возможно как плохо, так и хорошо.\n")
#         f.write("Плохое настроение, но мы его исправим.\n")
# except Exception as e:
#     print(f"Не удалось создать old.txt: {e}")
# print("\n-- Замена текста: 'плохо' на 'хорошо' ---")

# try:
#     with open(old_file_path, 'r' , encoding='utf-8') as old_file_stream:
#         old_content = old_file_stream.read()
#         print(f"Содержимое '{old_file_path}': \n{old_content}")
# except FileNotFoundError:
#     print(f"Ошибка: Файл '{old_file_path}' не найден")
#     exit()
# except Exception as e:
#     print(f"Произошла ошибука при чтении файла '{old_file_path}': {e}")
#     exit()
# new_content = re.sub(r'плохо', 'хорошо', old_content, flags=re.IGNORECASE)

# try:
#     with open(new_file_path, 'w', encoding='utf-8') as new_file_stream:
#         new_file_stream.write(new_content)
#         print(f"Замена выполнена. '{new_file_path}'.")
#         print(f"Содержимое. '{new_file_path}':\n{new_content}")
# except Exception as e:
#     print(f"Ошибка при записи файла '{new_file_path}': {e}")


# Задача 5
# Фильтрация строк
# Прочитай файл numbers.txt, в котором каждое число на отдельной строке. Создай новый файл even.txt, в который запиши только чётные числа из исходного файла.

# input_filename = "numbers.txt"
# output_filename = "even.txt"

# even_numbers_list = []

# print(f"Попытка чтения чисел из файла: '{input_filename}'")

# try:
#     with open(input_filename, 'r') as infile:
#         for line in infile:
#             try:
#                 num_str = line.strip()
#                 if not num_str:
#                     continue
#                 num = int(num_str)
#                 if num % 2 == 0:
#                     even_numbers_list.append(num)
#             except ValueError:
#                 print(f"Предупреждение: Пропущена нечисловая строка: '{line.strip()}'")
# except FileNotFoundError:
#     print(f"Ошибка: Файл '{input_filename}' не найден. Убедитесь, что он находится в той же директории, что и скрипт.")
#     exit()

# print(f"Найдено {len(even_numbers_list)} четных чисел.")
# print(f"Попытка записи четных чисел в файл: '{output_filename}'")

# try:
#     with open(output_filename, 'w') as outfile:
#         outfile.writelines(str(num) + '\n' for num in even_numbers_list)
#     print(f"Фильтрация завершена успешно! Четные числа сохранены в '{output_filename}'.")
# except IOError as e:
#     print(f"Ошибка при записи в файл '{output_filename}': {e}")