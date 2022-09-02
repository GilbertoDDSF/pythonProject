import forca
import adivinha

print("*********************************")
print("Escolha seu jogo!")
print("*********************************")

print("(1) Forca  (2)Adivinhacao")

jogo = int(input("Qual jogo quer jogar?"))

if jogo == 1:
    print("Jogando Forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhacao")
    adivinha.jogar()
