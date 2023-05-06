import random
import docx

path = 'output/'
num_files = 10
min_words = 100
max_words = 200

# Файл words1.txt содержит список слов, каждое слово записано в новой строке.
with open('words1.txt', 'r', encoding='utf-8') as f:
    words = f.readlines()


# Функция, которая будет генерировать случайный текст заданной длины из списка слов. Функция принимает список слов и
# заданный диапазон для количества слов в тексте. Она выбирает случайное количество слов в заданном диапазоне и собирает
# их вместе в случайный текст, разделяя слова пробелами и добавляя случайный знак препинания в конце.
def generate_text(words, min_words, max_words):
    num_words = random.randint(min_words, max_words)
    text = ''
    for i in range(num_words):
        word = random.choice(words).strip()
        if i == 0:
            word = word.capitalize()
        if i < num_words - 1:
            text += word + random.choice(['.', ',', ';', ':', '']) + ' '
        else:
            text += word + random.choice(['.', '!', '?'])
    return text


# В этом цикле мы создаем новый документ, генерируем случайный текст с помощью нашей функции и добавляем его в документ,
# сохраняя его в файл .docx в указанной папке. В path (строка 4) пользователь указывает путь к папке, в которой будут
# сохраняться созданные файлы. Пример пути: 'C:/Users/maxdy/Desktop/result/'
for r in range(num_files):
    doc = docx.Document()
    text = generate_text(words, min_words, max_words)
    doc.add_paragraph(text)
    doc.save(path + 'file{}.docx'.format(r))
