import random

print("O tema é FRUTA!!!")
palavras = ["morango", "maçã", "melancia", "abacaxi", "maracujá", "melão", "laranja", "pêra", "uva", "abacate",
            "acerola"]


def escolher_palavra():
    return random.choice(palavras)


def jogar_forca(palavra):
    tentativas = 6
    letras_erradas = []
    letras_corretas = []

    while True:
        estado_atual = ""
        for letra in palavra:
            if letra in letras_corretas:
                estado_atual += letra + " "
            else:
                estado_atual += "_ "
        print("Palavra:", estado_atual)

        if len(letras_erradas) > 0:
            print("Letras erradas:", " ".join(letras_erradas))

        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já escolheu essa letra. Tente novamente.")


        if letra in palavra:
            letras_corretas.append(letra)
        else:
            letras_erradas.append(letra)
            tentativas -= 1

        if all(letra in letras_corretas for letra in palavra):
            print("Parabéns! Você Acertou!", palavra)
            break
        elif tentativas == 0:
            print("Você perdeu. A palavra era:", palavra)
            break

        print("Tentativas restantes:", tentativas)
        print()

def main():
    print("Bem-vindo ao Jogo da Forca!")
    palavra = escolher_palavra()
    jogar_forca(palavra)

if __name__ == "__main__":
    main()