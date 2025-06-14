import random

dados = ['editar', 'galinha', 'laranja', 'cobra', 'carro', 'morango', 'óculos', 'colchão', 'navio']
palavra = random.choice(dados)

palavra_testada = ['_'] * len(palavra)

letras_tentadas = []

tentativa = 10



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
        print('Errou! Você tem mais ' + str(tentativa) + ' chances.')
    
    if '_' not in palavra_testada:
        print('\nParabéns, você acertou a palavra! ' + palavra)
        break
else:
    print('\nVocê perdeu! A palavra certa era: ' + palavra)
