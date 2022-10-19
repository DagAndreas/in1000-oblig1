dato1 = input("Vennligst skriv en dato(dd.mm): ")
dato2 = input("Vennligst skriv en dato som kommer senere(dd.mm): ")

#splitter string dato1 og dato2
dato1 = dato1.split(".")
dato2 = dato2.split(".")

print(dato1)
print(dato2)

if dato1 == dato2:
    print("Samme dato")
elif dato1[1] > dato2[1] or (dato1[1] == dato2[1] and dato1[0] > dato2[0]):
    print("Feil rekkefølge", dato1, "kommer etter", dato2)
elif dato1[1] < dato2[1] or (dato1[1] == dato2[1] and dato1[0] < dato2[0]):
    print("riktig rekkefølge", dato1, "kommer før", dato2)
