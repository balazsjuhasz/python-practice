from translate import Translator
translator = Translator(to_lang="ja")
try:
    with open('./input.txt', mode='r') as my_file:
        text = my_file.read()
        print(text)
        translation = translator.translate(text)
        print(translation)
        with open('./input-ja.txt', mode='w') as my_output:
            my_output.write(translation)
except FileNotFoundError as e:
    print('check your file path')
