import random

# Palavra secreta escolhida aleatoriamente
dados = ['editar', 'galinha', 'python', 'tiktok', 'laranja']
palavra = random.choice(dados)

# Lista de letras adivinhadas (substituídas por _ no início)
palavra_testada = ['_'] * len(palavra)

# Número de tentativas disponíveis
tentativa = 10

# Loop principal do jogo
while tentativa > 0:
    print('\nPalavra atual: ' + ' '.join(palavra_testada))
    
    palavra_escolhida = input('Digite uma letra: ').lower()

    if palavra_escolhida in palavra:
        for i in range(len(palavra)):
            if palavra[i] == palavra_escolhida:
                palavra_testada[i] = palavra_escolhida
        print('Ótima escolha!')
    else:
        tentativa -= 1
        print('Errou! Tente de nnovo: ' + str(tentativa))
    
    if '_' not in palavra_testada:
        print('\nParabéns, você acertou a palavra! ' + palavra)
        break
else:
    print('\nVocê perdeu! A palavra certa era: ' + palavra)
