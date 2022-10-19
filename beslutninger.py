#første spørsmål
svar1 = input("Vil du ha en brus? ja/nei: ")
#print(svar1)

#svar = ja
if svar1.lower() == "ja":
    print("Her har du en brus")

#svar = nei
elif svar1.lower() == "nei":
    print("Den er grei")

#hvis verken
else:
    print("Det forstod jeg ikke")
