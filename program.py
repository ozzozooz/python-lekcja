#l1"
import random
haslo = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
xyz = True
while xyz:
    lenght = int(input("podaj długość hasła"))
    for i in range(lenght):
        password += random.choice(haslo)

    print(password)
    decyzja = input("czy chcesz wygenerować nowe hasło? (tak/nie)")
    if decyzja == "tak":
        xyz = True
        password = ""
    else:
        xyz = False
