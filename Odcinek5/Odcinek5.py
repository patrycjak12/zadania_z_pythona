# PETLA WHILE, INSTRUKCJA SKOKU ( BREAK, CONTINUE )

i = 5
while i>0:  # warunek kontynuacji petli dopoki jest prawda(True)
    print("Odliczanie... ", i)
    i-=1
print("Koniec odliczania!")

j=0
while True:
    j+=1
    if j % 2==1:
        continue #wtedy nam przechodzi na poczatek - instruckja skoku
    print(j)
    if j>=10:
        break

# teraz zmieniamy to tak, zeby program pomijal wartosci j ktore sa nieparzyste
print("koniec")