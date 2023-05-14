"""
Projeto de jogo de adivinhação
"""

import random

print("*********************************")
print("Bem vindo ao jogo de ADIVINHAÇÃO!")
print("*********************************")

NUMERO_SECRETO = random.randrange(1, 101)
TOTAL_DE_TENTATIVAS = 0
PONTOS = 1000

print(NUMERO_SECRETO)

print("Qual o nível de dificuldade?")
print()
print("(1) - Fácil")
print()
print("(2) - Médio")
print()
print("(3) - Difícil")
print()

NIVEL = int(input("Qual o nível de dificuldade? "))

if NIVEL == 1:
    TOTAL_DE_TENTATIVAS = 15
elif NIVEL == 2:
    TOTAL_DE_TENTATIVAS = 10
else:
    TOTAL_DE_TENTATIVAS = 5

for RODADA in range(1, TOTAL_DE_TENTATIVAS + 1):
    print(f"Tentativa {RODADA} de {TOTAL_DE_TENTATIVAS}")
    print()

    CHUTE = int(input("Digite um número entre 1 e 100: "))
    print("Voce digitou --->", CHUTE)
    print()

    if CHUTE < 1 or CHUTE > 100:
        print("Você deve digitar um número entre 1 e 100!")
        print()
        continue

    ACERTOU = CHUTE == NUMERO_SECRETO
    NUMERO_MAIOR = CHUTE > NUMERO_SECRETO
    NUMERO_MENOR = CHUTE < NUMERO_SECRETO

    if ACERTOU:
        print(f"Parabéns, voce acertou e fez {PONTOS} pontos!")
        print()
        break
    else:
        if NUMERO_MAIOR:
            print("Seu chute foi maior que o número secreto")
            print()
        elif NUMERO_MENOR:
            print("Seu chute foi menor que o número secreto")
            print()
        PONTOS_PERDIDOS = abs(NUMERO_SECRETO - CHUTE)
        PONTOS = PONTOS - PONTOS_PERDIDOS

print("Fim do jogo.")
print()
