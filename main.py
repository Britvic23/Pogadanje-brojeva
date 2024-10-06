import random

def guess_the_number():
    print("Dobrodošli u igru 'Pogađanje brojeva'!")
    
    # Odabir razine težine
    while True:
        print("\nOdaberite razinu težine:")
        print("1. Lako (1-10)")
        print("2. Srednje (1-50)")
        print("3. Teško (1-100)")
        
        try:
            level = int(input("Unesite broj razine: "))
            if level == 1:
                max_number = 10
                break
            elif level == 2:
                max_number = 50
                break
            elif level == 3:
                max_number = 100
                break
            else:
                print("Molimo unesite valjan broj razine (1, 2 ili 3).")
        except ValueError:
            print("Unesite broj za razinu težine!")
    
    # Nasumični broj koji korisnik pokušava pogoditi
    secret_number = random.randint(1, max_number)
    attempts = 0

    # Glavna petlja igre
    while True:
        try:
            guess = int(input(f"Pogodite broj između 1 i {max_number}: "))
            attempts += 1

            if guess < 1 or guess > max_number:
                print(f"Broj mora biti između 1 i {max_number}!")
            elif guess < secret_number:
                print("Previše nisko! Pokušajte ponovo.")
            elif guess > secret_number:
                print("Previše visoko! Pokušajte ponovo.")
            else:
                print(f"Čestitamo! Pogodili ste broj {secret_number} u {attempts} pokušaja!")
                break

        except ValueError:
            print("Molimo unesite valjani broj.")

# Pokretanje igre
guess_the_number()
