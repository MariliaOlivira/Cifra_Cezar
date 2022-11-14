from curses.ascii import isdigit
import string
alfa = list(string.ascii_lowercase) 

encode = input("Digite uma letra coisa linda: ")
key = int(input("Digite a chave: "))

answer = ''

for i in encode:
    if i == ' ':
        answer += ' '
        continue
    index = alfa.index(i)
    answer += alfa[index + (key)]


print(answer)





