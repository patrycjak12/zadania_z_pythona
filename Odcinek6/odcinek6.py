#MINI GRA - ZGADNIJ LICZE
import random

x=random.randint(1, 50) # losujemy liczbe calkowita z przedzialu od 1 do 50
# print(randint(1,10))
print("Wylosowalem liczbe z zakresu od 1 do 50! Spróbuj ją zgadnąć.")
i=0

while(True):
    i+=1
    y = int(input("Podaj liczbę: "))
    if x == y:
        break
    elif x < y:
        print("Liczba jest za duza! To jest twoja ", i , " próba. ")
    else:
        print("Liczba jest za mala! To jest twoja ", i , " próba. ")


print("Brawo! Udalo ci sie zgadnąć liczbę za ", i , " razem!")