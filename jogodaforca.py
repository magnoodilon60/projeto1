from random import randint


def iniciar_jogo():
    numero_secreto = randint(1,5)
    numero_escolhido = 0


    while True:
        try:
            numero_escolhido = int(input("Escolha um número de 1 a 5: "))
        except:
            print("Você escolheu un número inválido!!!")
        else:
            if numero_escolhido not in (1, 2, 3, 4, 5):
                print("Número precisa estar entre 1 e 5:")
                continue
            elif numero_escolhido == numero_secreto:
                print(f'parabéns!! Você descobriu que o número secreto era o {numero_secreto} !!!')
                break
            else:
                print("Você errou!!!")



iniciar_jogo()

