from interface import *
from manipulacao_dados import *
import os


def clear():
    os.system("cls||clear")


def continuar():
    input("\nPressione ENTER para continuar...")


def app():
    while True:
        clear()
        opcao = interface_usuario()

        if opcao == '1':
            clear()
            sacar()
            continuar()
        elif opcao == '2':
            clear()
            depositar()
            continuar()
        elif opcao == '3':
            clear()
            extrato()
            continuar()
        elif opcao == '4':
            clear()
            print("Saindo... \n")
            break
        else:
            print("Escolha uma opção válida...")


if __name__ == "__main__":
    app()
