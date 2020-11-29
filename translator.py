# File I/O: Translator
# A tool that reads a text file then translates them in another language (Japanese)
from translate import Translator
translator = Translator(to_lang="ja")
try:
    with open('./test.txt', mode='r') as my_file:
        translation = translator.translate(my_file.read())
        print(translation)
        with open('./test-ja.txt', mode='w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('File not found')