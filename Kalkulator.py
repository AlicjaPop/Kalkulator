import logging
logging.basicConfig(level=logging.DEBUG)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operation=input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

for text in operation:
    if text=="1":
        num_1=input("Podaj pierwszą liczbę:")
        num_2=input("Podaj drugą liczbę:")
        try:
            num_1=float(num_1)
            num_2=float(num_2) 
            logging.debug(f"Dodaję liczby {num_1} oraz {num_2}")
            print("Wynik to:", add(num_1,num_2))
        except ValueError:
            logging.debug("Podano nieprawidłową wartość.")
            continue
    elif text=="2":
        num_1=input("Podaj pierwszą liczbę:")
        num_2=input("Podaj drugą liczbę:")
        try:
            num_1=float(num_1)
            num_2=float(num_2)
            logging.debug(f"Odejmuję od liczby {num_1} liczbę {num_2}")
            print("Wynik to:", subtract(num_1,num_2))
        except ValueError:
            logging.debug("Podano nieprawidłową wartość.")
            continue
    elif text=="3":
        num_1=input("Podaj pierwszą liczbę:")
        num_2=input("Podaj drugą liczbę:")
        try:
            num_1=float(num_1)
            num_2=float(num_2) 
            logging.debug(f"Mnożę liczbę {num_1} przez liczbę {num_2}") 
            print("Wynik to:", multiply(num_1,num_2))
        except ValueError:
            logging.debug("Podano nieprawidłową wartość.")
            continue
    elif text=="4":
        num_1=input("Podaj pierwszą liczbę:")
        num_2=input("Podaj drugą liczbę:")
        try:
            num_1=float(num_1)
            num_2=float(num_2)
            logging.debug(f"Dzielę liczbę {num_1} przez {num_2}")
            print("Wynik to:", divide(num_1,num_2))
        except ValueError:
            logging.debug("Podano nieprawidłową wartość.")
            continue
    else:
        print("Podano nieprawidłową liczbę.")