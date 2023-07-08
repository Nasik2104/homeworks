import googletrans

Translator = googletrans.Translator()



def read_translate(Translator, file1):
    with open(file1, "r", encoding = 'utf-8') as my_file:
        text = my_file.read()
        global test
        test = Translator.translate(text, dest = 'en')
        print(test)

def write_translated_text(file2, test):
    with open(file2, 'w') as write:
        write.write(test.text)

file1 = "E:\\python_work\\homework\\06_07\\text.txt"
file2 = "E:\\python_work\\homework\\06_07\\text2.txt"

read_translate(Translator, file1)
write_translated_text(file2, test)
