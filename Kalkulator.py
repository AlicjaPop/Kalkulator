import logging
logging.basicConfig(level=logging.DEBUG)

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

operation=input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

for text in operation:
    if text=="1":
        num_text=input("Podaj liczby, które chcesz do siebie dodać, rozgraniczając je przecinkiem:")
        try:
            num_list=num_text.split(",")
            result=0
            for num in num_list:
                num=float(num)
                result=result+num
            logging.debug(f"Dodaję liczby {num_list}")
            print(f"Wynik to: {result}.")
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
        num_text=input("Podaj liczby, które chcesz przez siebie pomonożyć, rozgraniczając je przecinkiem:")
        try:
            num_list=num_text.split(",")
            result=1
            for num in num_list:
                num=float(num)
                result=result*num 
            logging.debug(f"Mnożę liczby {num_list}.") 
            print(f"Wynik to: {result}.")
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