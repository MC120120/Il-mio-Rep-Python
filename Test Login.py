# Sorprendi i tuoi compagni!
# 1. printa python pro
import time
import random

Credenziali = None

Login = input("Login o Sign up? ").strip().lower()

if Login == "sign up":
    CredenzialiNomeUtente = input("inserisci il tuo nome utente: ").strip()
    Nome = input("Inserisci il tuo nome Completo: ").strip()
    CredenzialiPassword = input("Inserisci la tua password: ").strip()
    Credenziali = [CredenzialiNomeUtente, Nome, CredenzialiPassword]
    for i in range(6):
        print("-")
        time.sleep(1)
        print("\\")
        time.sleep(1)
        print("|")
        time.sleep(1)
        print("/")

    print("Registrazione completata!")

elif Login == "login":
    if Credenziali is None:
        print("Devi prima creare un account con 'Sign Up'.")
    else:
        NomeUtente = input("Nome Utente per il Login: ").strip()
        Password = input("Password per il login: ").strip()
        if NomeUtente == Credenziali[0] and Password == Credenziali[2]:
            for i in range(6):
                print("-")
                time.sleep(1)
                print("\\")
                time.sleep(1)
                print("|")
                time.sleep(1)
                print("/")
            print("Benvenuto", Credenziali[1], "!")

            parole = ["Ciao!", "Python Pro", "Kodland"]
            print("Benvenuto al tuo corso di", parole[1], "!")

            emojis = ["^_^", "0_o", ":)", "-_-", "(￢_￢)"]
            print(random.choice(emojis))
        else:
            for i in range(6):
                print("-")
                time.sleep(1)
                print("\\")
                time.sleep(1)
                print("|")
                time.sleep(1)
                print("/")
            print("Password o nome utente errati")

else:
    print("Scelta non valida. Scrivi 'Login' o 'Sign Up'.")
