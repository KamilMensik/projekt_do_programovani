def file_load():
    while True:
        soubor = ''
        file_path = input('Vlozte nazev souboru: ')
        try:
            soubor = open(file_path, encoding='utf-8')
            return soubor
        except:
            print('Soubor nebyl nalezen.')


def file_lines_to_list(file) -> list:
    print(file.read().splitlines())

file_lines_to_list(file_load())