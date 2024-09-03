from modules.biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    try:
        pasirinkimas = int(input(
            "1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n9 - išeiti iš programos\n"))
    except ValueError:
        print("Prašome įvesti skaičių.")
        continue

    if pasirinkimas == 1:
        while True:
            try:č
                suma = float(input("Įveskite pajamų sumą: "))
                break
            except ValueError:
                print("Neteisinga suma, bandykite dar kartą.")
        siuntejas = input("Įveskite siuntėją: ")
        papildoma_info = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_info)
    elif pasirinkimas == 2:
        while True:
            try:
                suma = float(input("Įveskite išlaidų sumą: "))
                break
            except ValueError:
                print("Neteisinga suma, bandykite dar kartą.")
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        preke_paslauga = input("Įveskite įsigytą prekę/paslaugą: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, preke_paslauga)
    elif pasirinkimas == 3:
        print(f"Balansas: {biudzetas.gauti_balansa()}")
    elif pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
    elif pasirinkimas == 9:
        print("Viso gero")
        break
    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")
