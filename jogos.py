"""
Projeto Sistema de Jogos
"""

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) - FORCA")
print()

print("(2) - ADIVINHACAO")
print()

print("(3) - SAIR")
print()

JOGO = int(input("Qual jogo? "))

if JOGO == 1:
    print("Jogando FORCA")
elif JOGO == 2:
    print("Jogando ADIVINHACAO")
else:
    print("Você escolheu sair")
    print()
