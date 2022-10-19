#mulighet til å endre spørsmål senere
spsm = ("Velkommen. Vennligst skriv navnet ditt her: ")

#spørsmål og svarinput
navn1 = input(f"{spsm}")
print("Hei", navn1)
print(" ")

#variabel a og b uten input
a = 100
b = -100
print("a  = ", a)
print("b  = ", b)


#regne på differanse
c = a - b
print("Differanse:", c)
print(" ")

#nytt navn
navn2 = input("Gi meg et navn til: ")

#navn sammen
sammen = navn1 + " og " + navn2
print("Navnene er ", sammen)
