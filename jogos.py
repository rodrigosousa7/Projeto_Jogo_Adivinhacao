"""
Projeto Sistema de Jogos
"""
import forca
import adivinhacao

def escolhe_jogo():
    print("***********************************")
    print("******* Escolha o seu jogo! *******")
    print("***********************************\n")

    print("(1) - FORCA\n\n(2) - ADIVINHACAO\n\n(3) - SAIR\n")

    while True:
        jogo = int(input("Qual jogo? "))
        print()

        if jogo == 1:
            print("Jogando FORCA\n")
            forca.jogar()
            break
        if jogo == 2:
            print("Jogando ADIVINHACAO\n")
            adivinhacao.jogar()
            break
        if jogo == 3:
            print("Você escolheu sair\n")
            break
        print("Opção inválida. Escolha 1, 2 ou 3.\n")

if __name__ == "__main__":
    escolhe_jogo()
