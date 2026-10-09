print("Kolejność:")

print((2 + 2) * 2)  #do dyspozycji mamy tylko nawiasy okrągłe



print("Dzielenie:")

print(5/2)         # odrazu mamy dzielenie zmiennoprzecinkowe
print(5//2)        # dzielenie calkowite (ile zmiescilo sie liczb w calosci



print("Mnożenie:")

print(2*3)

print(2 ** 3)  # podstawa potegowania to 2, a potęga to 3



print("Skrócone:") # mozemy skrocic wczesniejsze operacje # x++ - blad;
x = 5
x += 1
print(x)



print("Konwersja:") #konwersja typow, int, bool, string, float, double,

a=input("Podaj liczbe: ") #zwraca nam string
b=input("Podaj liczbe: ") #zwraca nam string

#a=int(a)

print(a + b) # czyli np 3 + 1 = 31 bo dokleily sie liczby to jest dalej string ale

a=int(a) # a liczby zmiennoprzecinkowe to float(a) float(b) liczby odzielamy kropka
b=int(b)

print(a + b)

y='2'
z='2'
print(y + z)

j=2
g=2
print(str(j) + str(g))

del j # pozbycie sie zmiennej j
print(str(j) + str(g))



