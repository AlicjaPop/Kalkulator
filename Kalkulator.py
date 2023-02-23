def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

text=input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
num_1=float(input("Podaj pierwszą liczbę:"))
num_2=float(input("Podaj drugą liczbę:"))


print("Dodaję", num_1, "oraz", num_2)
print("Wynik to:", add(num_1,num_2))

