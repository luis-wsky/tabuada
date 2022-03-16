# Tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
print('-' * 50)
print('                   \033[1;30;44m TABUADA \033[m')
print('-' * 50)
tabuada = int(input('Escolha um número para a TABUADA que deseja saber:'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(tabuada, c, tabuada * c))
