Wordlists Generator
----

## Descrição

Esse gerador de Wordlist recebe uma lista de palavras chave e aplica transformações a fim de gerar o máximo de chaves possíveis nesse contexto.

## Parâmetros 

**ENTRADA**: Lista de palavras escrita pelo usuario como uma string separada por ' ' ou ','. Podendo ser alterado na variável ``regex``.
**SAIDA**: Arquivo de texto com todas as possibilidades de palavras geradas.

## Variáveis
É possível alterar algumas variáveis para conforto do usuário
**``regex``**: Expressão regular que permite pegar várias palavra de uma vez só na string de entrada do usuário.
**``path``**: Caminho aonde o arquivo de wordlists deve ser escrito.

## Funções
``upper_lower_and_capitalize``: Gera variantes da palavra em caracteres maiusculos, minusculos e capitalizado.
``concat_upper_lower_and_capitalize``: Gera variantes das palavras chave concatenadas com suas variantes em caracteres maiusculos, minusculos e capitalizado.
``concat_words``: Gera variantes concatenadas por meio da função ``concat_upper_lower_and_capitalize``.
``concat_reversed_words``: Gera variantes concatenadas com palavras invertidas.
``word_with_numbers``: Gera variantes com lista de numeros de 0 a 9.
### Regex Cheat Sheet
SYMBOL | MEANING |
 --- | --- |
[]	| A set of characters		
\	| Signals a special sequence (can also be used to escape special characters)		
.	| Any character (except newline character)	
^	| Starts with	
$	| Ends with		
*	| Zero or more occurrences		
+	| One or more occurrences		
?	| Zero or one occurrences		
{}	| Exactly the specified number of occurrences		
|	| Either or	
()	| Capture and group