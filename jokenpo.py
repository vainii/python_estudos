import random

escolhas = ['Pedra', 'Papel', 'Tesoura']

jogador = int(input('Escolha Pedra, Papel ou Tesoura:\n Digite 1 para Pedra, 2 para Papel e 3 para Tesoura:\n '))
print(f'Você escolheu {escolhas[jogador - 1]}')

computador = random.randint(0, 2)
print(f'O computador escolheu {escolhas[computador]}')

ganha_de = {
    0: 2, # Pedra ganha de tesoura
    1: 0, # Papel ganha de pedra
    2: 1  # Tesoura ganha de papel  
}

if jogador == computador + 1:
    print('Empate!') 
elif ganha_de[jogador - 1] == computador:
    print('Você ganhou!')
else:
    print('Você perdeu!')
