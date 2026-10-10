wiek = 11
kasa = 10

# if wiek>=18:
#    if kasa>=40:
#        print("Mozesz wejsc na film. ")
#    else:
#        print("Nie mozesz wejsc na film. ")
#
# else:
#     print("Nie mozesz wjesc na film. ")

#Skrocona wersja kodu

#if (wiek>=18) and (kasa>=40):  # obie rzeczy musza być spełnione
#    print("Mozesz wejsc na film. ")

if wiek<=12 or kasa>=30: # to lub to moze byc spelnione albo obie rzeczy
    print("Mozesz wejsc!")

if not(wiek>12) or kasa>=30: # not sluszy do negacji - true na false i false na true zamienia
    print("Mozesz wejsc!")


if True or True and False: # and (mnozenie) ma wiekszy priorytet nad suma (or)
    print("Prawda")
else:
    print("Fałsz")

