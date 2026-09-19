# Sorprendi i tuoi compagni!
# 1. printa python pro
import time
Login = input("Login o Sign up?")

if Login == "Sign Up":
    CredenzialiNomeUtente = input("inserisci il tuo nome utente")
    Nome = input("Inserisci il tuo nome Completo")
    CredenzialiPassword = input("Inserisci la tua password")
    Credenziali = [CredenzialiNomeUtente, Nome, CredenzialiPassword]
    for i in range (6):
        print("-")
        time.sleep(1)
        print("\\")
        time.sleep(1)
        print("|")
        time.sleep(1)
        print("/")      
        

if Login == "Login":
    NomeUtente = input("Nome Utente per il Login")
    Password = input("Password per il login")
    if NomeUtente == (Credenziali[2]) and NomeUtente == (Credenziali[0]):
        for i in range (6):
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

        import random
        emojis = ["^_^", "0_o", ":)", "-_-", "(￢_￢)"]
        print(random.choice(emojis))

    else: 
        for i in range (6):
            print("-")
            time.sleep(1)
            print("\\")
            time.sleep(1)
            print("|")
            time.sleep(1)
            print("/") 
        print("Password o nome utente Errati")
            
