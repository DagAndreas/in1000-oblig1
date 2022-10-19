#i for loop
i = 1

#brukerinput for første dag
while i < 2:
    dato1dag = input("skriv inn en dag(1-31): ")
    #tester etter gyldig første dag
    if dato1dag.isdigit():
        if int(dato1dag) > 31 or int(dato1dag) < 1:
            print("ugyldig tall")
            continue
        break
    else:
        print("IKKE ET TALL ENGANG")

#brukerinput for første mnd
while i < 2:
    dato1mnd = input("skriv inn en måned(1-12): ")
    if dato1mnd.isdigit():
        #tester etter gyldig første mnd
        if int(dato1mnd) > 12 or int(dato1mnd) < 1:
            print("ugyldig tall")
            continue
        break
    else:
        print("IKKE ET TALL ENGANG")

print("Vennligst skriv en dato som kommmer etter", dato1dag + "." + dato1mnd)


#brukerinput for andre dato
while i < 2:
    dato2dag = input("skriv inn en dag(1-31): ")
#tester etter gyldig 2. dag
    if dato2dag.isdigit():
        if int(dato2dag) > 31 or int(dato2dag) < 1:
            print("ugyldig tall")
            continue
        break
    else:
        print("IKKE ET TALL ENGANG")


while i < 2:
    dato2mnd = input("skriv inn enda en måned(1-12): ")
    #tester etter gyldig 2. m
    if dato2mnd.isdigit():
        if int(dato2mnd) > 12 or int(dato2mnd) < 1:
            print("ugyldig tall")
            continue
        break
    else:
        print("IKKE ET TALL ENGANG")

dato2 = dato2dag, ".", dato2mnd
print("Den andre datoen er:", dato2)

#gjør om streng til tall
dato1dag = int(dato1dag)
dato1mnd = int(dato1mnd)
dato2dag = int(dato2dag)
dato2mnd = int(dato2mnd)

#samme dato
if dato2mnd == dato1mnd and dato2dag == dato1dag:
    print("Samme dato:")
    print(dato1dag, ".", dato1mnd, "er det samme som", dato2dag, ".", dato2mnd)
#hvis 1. dato er høyere enn 2. dato = feil
elif dato2mnd < dato1mnd or dato2dag < dato1dag:
     print("Feil rekkefølge:")
     print(dato1dag,  ".", dato1mnd, "kommer etter", dato2dag, ".", dato2mnd)
#hvis 1. dato er lavere enn 2. dato = riktig
elif dato2mnd > dato1mnd or dato2dag > dato1dag:
    print("Riktig rekkefølge:")
    print(dato1dag,  ".", dato1mnd, "kommer før", dato2dag, ".", dato2mnd)

else:
    print("Det forstod jeg ikke")
