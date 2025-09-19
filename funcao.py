# criar umjogo de forca onde o usuario tenta adivinhar uma palavra secreta,
# letra por letra, com ate 6 erros permitido.

import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta= carrega_palavra_secreta()
    letras_acertadas= inicializa_letras_acertadas(palavra_secreta)
    print (letras_acertadas)

    enforcou= False
    acertou= False
    erros=0

    while(not enforcou and not acertou):
        chute= pede_chute()

        if chute in palavra_secreta:
            index= 0
            for letra in palavra_secreta:
                if chute==letra:
                    letras_acertadas[index]=letra
                index+=1
        else:
            erros+=1

            enforcou= erros ==6
            acertou= '_' not in letras_acertadas
            print(letras_acertadas)

    if acertou:
        print('voce ganhou')
    else:
        print('voce perdeu')
    print('fim de jogo')

def pede_chute():
        chute= input('qual a letra? ')
        chute= chute.strip(). lower()
        return chute

def imprime_mensagem_abertura():
        print('*************************************')
        print('****** bem vindo ao jogo da forca****')
        print('*************************************')

def carrega_palavra_secreta(nome_do_arquivo= r'C:\Users\Aluno_Programador2\Desktop\jogo\palavras_forca.txt'):
    arquivo=open(nome_do_arquivo, 'r')
    palavras=[]

    for linha in arquivo:
        linha=linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero=random.randrange(0, len(palavras))
    palavras_secretas = palavras[numero].lower()

    return palavras_secretas

def inicializa_letras_acertadas(palavra):
    return['_' for letra in palavra]

if __name__ == '__main__':
  jogar()




