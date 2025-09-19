import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(' '.join(letras_acertadas))  # Melhor exibir assim

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = letra
        else:
            erros += 1
            print(f"Você errou! Tentativas restantes: {6 - erros}")

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(' '.join(letras_acertadas))

    if acertou:
        print('Você ganhou!')
    else:
        print(f'Você perdeu! A palavra era "{palavra_secreta}".')
    print('Fim do jogo')

def pede_chute():
    chute = input('Qual a letra? ').strip().lower()
    return chute

def imprime_mensagem_abertura():
    print('********************************************')
    print('******* Bem vindo ao jogo da Forca! ********')
    print('********************************************')

def carrega_palavra_secreta(nome_do_arquivo=r'C:\Users\Aluno_Programador2\Desktop\jogo\palavras_forca.txt'):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            palavras = [linha.strip() for linha in arquivo if linha.strip()]
        if not palavras:
            print("Arquivo de palavras está vazio.")
            exit()
        numero = random.randrange(len(palavras))
        palavra_secreta = palavras[numero].lower()
        return palavra_secreta
    except FileNotFoundError:
        print(f"Arquivo {nome_do_arquivo} não encontrado.")
        exit()

def inicializa_letras_acertadas(palavra):
    return ['_' for _ in palavra]

if __name__ == '__main__':
    jogar()
