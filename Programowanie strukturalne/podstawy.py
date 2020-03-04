print("CDV")
print(10)
'''
komentarz
blokowy
'''
#Potęgowanie

potega=2 ** 10
print(potega)

#Pobieranie danych z klawiatury

name=input()
# + konkatenacja
print("Twoje imię: " + name)
surname=input()
print("Twoje imie: " +name+", Nazwisko: " +surname)

'''
Uzytkownik podaje z klawiatury swój wiek
Wyświetl dane w formacie: Twój wiek: ... lat
'''

print("Podaj swój wiek: ",end="")
age=input()
print(type(age))
print("Twój wiek: ", age, " lat")
age1=20
print(type(age1))

surname="Kowalski"
firstletter=surname[0]
print(firstletter)
length=len(surname)
print(length)

lastLetter=surname[-1]
print(lastLetter)

