"""
Projeto de jogo de adivinhação
"""

import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de ADIVINHAÇÃO!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?\n")
    print("(1) - Fácil\n\n(2) - Médio\n\n(3) - Difícil\n")

    nivel = int(input("Qual o nível de dificuldade? "))
    while nivel not in (1, 2, 3):
        nivel = int(input("Digite o valor correspondente ao nível: "))
        print()

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 15
    else:
        total_de_tentativas = 10

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}\n")

        # A função "input" sempre retorna um string. Você deve converter com a função "int"
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Voce digitou --->", chute)
        print()

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!\n")
            continue

        acertou = chute == numero_secreto
        numero_maior = chute > numero_secreto
        numero_menor = chute < numero_secreto

        if acertou:
            print(f"Parabéns, voce acertou e fez {pontos} pontos!\n")
            break

        if numero_maior:
            print("Seu chute foi maior que o número secreto\n")

        elif numero_menor:
            print("Seu chute foi menor que o número secreto\n")
            pontos_perdidos = round(abs(chute - numero_secreto) / 3) # dividindo por três
            pontos = pontos - pontos_perdidos # subtraindo os pontos perdidos da pontuação total

        if rodada == total_de_tentativas:
            print(f"O número secreto era: {numero_secreto}. Você fez {pontos}\n")

    print("Fim do jogo.\n")

if __name__ == "__main__":
    jogar()
