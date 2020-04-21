# Esercizio 2
# Autore: Pasquale
# Data: 20 aprile 2020

def CountWords():
    
    answer = 'S'
    while answer == 'S':

        import os
        import re

        print('')
        file_name = input(f'Inserisci il nome del file di testo: ')
        print('')

        lista_files = os.listdir()
        match = re.search('\\b'+file_name+'\\b', str(lista_files))

        if match:

            try:
                text = open(file_name, 'r')
                stringa_text = text.read()
            
                stringa_text_filtered = re.sub(r'[\.\,\'\[\]\"\?\!\*\:\;\n\-\(\)\{\}]', r'', stringa_text, flags=re.MULTILINE).lower()
                lista_text_split = re.split(r'[\s]', stringa_text_filtered)
                lista_text_split = ' '.join(lista_text_split).split()

                unique_text_split = set(lista_text_split)
                dict_words = {}

                for words in unique_text_split : 
                        dict_words[words] = lista_text_split.count(words)

                print(dict_words)

            except FileNotFoundError:
                print('Attenzione il file inserito non è presente!')

        else:
            print('')
            print('Attenzione il file inserito non è presente!')
            print('')

        print('')
        answer = input('Vuoi continuare? S/n: ')

CountWords()