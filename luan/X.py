print('Olá, me chamo X, sou um bot em aprendizado.')

print('Qual o seu nome?')

nome = input('>: ')

print(f'Prazer em te conhecer {nome}!')

print('Como você está se sentindo?')

condicao = input('>: ')

arquivo = open('resposta.txt', "r")
condicoes = []

if condicao == condicao:
    print('Fico feliz em saber disso =)')
else:
    print('Relaxa, as coisas vão melhorar ;)')

print('Por enquanto é isso... Acho que é hora de dar "Tchau"')
resposta = input('>: ')
if resposta == 'Tchau':
    print('Tchau tchau!')
quit()
