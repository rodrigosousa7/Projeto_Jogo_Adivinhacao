"""
Projeto de jogo de forca
"""

import random

def jogar():
    """
    Função para interligar o jogo de adivinhação com o módulo principal (jogos.py)
    """
    imprime_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    letras_faltando = imprime_letras_faltando(palavra_secreta)
    print(letras_acertadas)
    print()
    print(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            letras_faltando = marca_chute_correto(chute, letras_acertadas, palavra_secreta, letras_faltando)
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {len(palavra_secreta)-erros} tentativas.\n")

        enforcou = erros == len(palavra_secreta)
        print(' '.join(letras_acertadas))
        print()

        if letras_faltando == 0:
            acertou = True

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo.\n")


def imprime_abertura():
    """
    Função imprimir abertura
    """
    print("*"*33)
    print("** Bem vindo ao jogo de FORCA! **")
    print("*"*33)
    print()


def carrega_palavra_secreta():
    """
    Função para carregar palavra secreta diretamente do arquivo txt
    """
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    """
    Função para preenchimento de espaços de palavras com de acordo com a quantidade de letras
    """
    letras_acertadas = ["_"] * len(palavra_secreta)
    return letras_acertadas


def imprime_letras_faltando(palavra_secreta):
    """
    Função para imprimir as letras faltantes
    """
    letras_faltando = len(palavra_secreta)
    print(f"Ainda faltam acertar {letras_faltando} letras:")
    return letras_faltando


def pede_chute():
    """
    Função para pedir chute do usuário
    """
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    print()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta, letras_faltando):
    """
    Função para marcar os chutes correto do usuário
    """
    for index, letra in enumerate(palavra_secreta):
        if chute == letra:
            letras_acertadas[index] = letra
            letras_faltando -= 1
            index += 1
    return letras_faltando


def imprime_mensagem_vencedor():
    """
    Função para imprimir mensagem ganhador, caso todas as palavras estejam corretas
    """
    print("Parabéns, você acertou a palavra secreta!\n")


def imprime_mensagem_perdedor(palavra_secreta):
    """
    Função para imprimir mensagem perdedor, caso o usuário erre todas as tentativas
    """
    print("Que pena, você não conseguiu acertar a palavra secreta.\n")
    print(f"A palavra era {palavra_secreta}\n")

if __name__ == "__main__":
    jogar()
