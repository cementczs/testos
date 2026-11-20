
import random

tajne_cislo = random.randint(1, 100)
pocet_pokusu = 0

print("🎮 Pojď si zahrát hru Hádej číslo")
print("Myslím si číslo od 1 do 100.")

while True:
    try:
        tip = int(input("Zadej svůj tip: "))
    except ValueError:
        print("Zadej prosím celé číslo!")
        continue

    if tip < 1 or tip > 100:
        print("Číslo musí být od 1 do 100.")
        continue

    pocet_pokusu += 1

    if pocet_pokusu == 5:
        if tajne_cislo % 2 == 0:
            print("Nápověda: Hledané číslo je sudé")
        else:
            print("Nápověda: Hledané číslo je liché")
    

    if tip < tajne_cislo:
        print("Hledané číslo je VĚTŠÍ.")
    elif tip > tajne_cislo:
        print("Hledané číslo je MENŠÍ.")
    else:
        print(f"🎉 Správně! Uhodl jsi číslo {tajne_cislo}.")
        print(f"Počet pokusů: {pocet_pokusu}")
        break
