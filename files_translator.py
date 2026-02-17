from translate import Translator

translator = Translator(to_lang="hi")

try:
    with open("testing.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        # Once translated create a new file for translation text
        with open("translated.txt", mode="w") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("No such file found! Check the file path or if file exists.")