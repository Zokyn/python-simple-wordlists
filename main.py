import re

# Variaveis 
regex = r'\s*,\s*|\s+' # pattern usado na detecção de palavras no input
path = 'wordlist.txt'  # caminho de destino aonde será criado o wordlist

# Funções
def upper_lower_and_capitalize(word, array):
    array.append(word.lower())
    array.append(word.upper())
    array.append(word.capitalize())

    return array

def concat_upper_lower_and_capitalize(word, another_word, array):
    a_word = [word, word.upper(), word.lower(), word.capitalize()]
    a_another_word = [another_word, another_word.upper(), another_word.lower(), another_word.capitalize()]
    for _word in a_word:
        for _another_word in a_another_word:
            if(array.count(_word+_another_word) == 0): 
                array.append(_word+_another_word)
                word_with_numbers(_word+_another_word, array)

def concat_words(list, array):
    for word in list:
        for another_word in list:
            concat_upper_lower_and_capitalize(word, another_word, array)

def concat_reversed_words(list, array):
    for word in list:
        word = word[::-1]
        for another_word in list:
            another_word = another_word[::-1]
            concat_upper_lower_and_capitalize(word, another_word, array)

def word_with_numbers(word, array):
    numberstring = ''
    i = 0
    for i in range(10):
        numberstring = numberstring + str(i)
        array.append(word+str(i))    
        array.append(word+str(numberstring))    
        array.append(word+str(numberstring)[::-1])
        
############################### INICIO DO CODIGO #############################
print('-----WORDLIST GENERATOR------')
### RECEBE LISTA DE PALAVRAS CHAVE 
print("Insira as palavras chave. Utilize ',' ou ' ' para separar")
keywords = input('PALAVRAS-CHAVE: ').strip()
print(f'1.\tINPUT: {keywords}')
keywords = re.split(regex, keywords); 
print(f'2.\tKEYWORDS: {keywords}')

### GERA PALAVRAS DERIVADAS
temp_word = ''
wordlist = []
### VARIANTES DA PALAVRAS CHAVE
## Variantes maiúsculas, minusculas e capitalizadas
for word in keywords:
    upper_lower_and_capitalize(word, wordlist)
## Variantes reversas
for word in keywords:
    upper_lower_and_capitalize(word[::-1], wordlist)
## Variantes concatenadas (maiusculas/minusculas/cap.)
for word in keywords:
    concat_words(keywords, wordlist)
## Variantes concatenadas com palavras invertidas
for word in keywords:
    concat_reversed_words(keywords, wordlist)
## Variantes com possiveis combinações de numeros
for word in keywords:
    word_with_numbers(word, wordlist)

with open(path, 'w') as f:
    for word in wordlist:
        f.write(word + '\n')

print(f'3.\tLocal do Arquivo: ./{path}')
print(f'4.\tNumero de Palavas: {len(wordlist)}')
#############################################################################