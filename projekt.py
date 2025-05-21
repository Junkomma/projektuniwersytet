import json
import re
def poprawnosc(tekst):
    tekst = tekst.strip().lower()
    tekst = re.sub(r'\s+', ' ', tekst)
    return tekst

wydz = ("Wydział Archeologii","Wydział Biologii","Wydział Chemii","Wydział Dziennikarstwa, Informacji i Bibliologii")
uni1 = "Uniwersytet Warszawski"
uni2 = "Uniwesrsytet Wroclawski UWr"
uni3 = "Uniwersytet Krakowski Jagiellońskiego"
print("Witamy w dzienniku studentów!")
print('Jakie są wydziały:')
#dane: kierunki sdudiow

k_st = {
    "Uniwersytet Warszawski": ["Wydział Archeologii","Wydział Biologii","Wydział Chemii","Wydział Dziennikarstwa, Informacji i Bibliologii"],
    "Uniwesrsytet Wroclawski UWr": ["Wydział Archeologii","Wydział Biologii","Wydział Chemii","Wydział Dziennikarstwa, Informacji i Bibliologii"],
    "Uniwersytet Krakowski Jagiellońskiego": ["Wydział Archeologii","Wydział Biologii","Wydział Chemii","Wydział Dziennikarstwa, Informacji i Bibliologii"]
}
#dane studentow
st = {"Przykład dannych" : ['Imię','Nazwisko','Data urodzenia','Wydział'],
    "Uniwersytet Warszawski" : [['Kasia','Bogdanowska','21.07.2005','Wydział Biologii'],['Ola','Gliwińska','06.05.2005','Wydział Chemii']],
"Uniwesrsytet Wroclawski UWr" : [['Maja','Targowska','03.03.2004','Wydział Nauk Historycznych i Pedagogicznych'], ['Maciej','Bujok','02.01.2005','Wydział Nauk Społecznych']],
"Uniwersytet Krakowski Jagiellońskiego": [['Roman','Podlaski','12.01.2004','Wydział Matematyki i Informatyki'],['Arkadiusz','Hinc','03.10.2004','Wydział Matematyki i Informatyki']]

}
#Zapisanie danych wydzialow do pliku typu JSON

with open("k_st.json", "w", encoding="utf-8") as plik:
    json.dump(k_st, plik, ensure_ascii=False, indent=4)

#Zapisywanie danych studentow do pliku typu json

with open("st.json", "w", encoding="utf-8") as plik:
    json.dump(st, plik, ensure_ascii=False, indent=4)
#wyswietlanie danych z pliku json

with open("k_st.json", "r", encoding="utf-8") as plik:
    k_st = json.load(plik)
    for key, wartosc in k_st.items():
        print(f"{key}: {wartosc}")

#wyswietlanie danych z pliku json
with open("st.json", "r", encoding="utf-8") as f:
    st = json.load(f)
    for key, wartosc in st.items():
        print(f"{key}: {wartosc}")


#wprowadzanie nowych dannych o nowym studencie
nowy_st = []

a = str(input('Czy chcesz wprowadzic nowe dane?:'))
if a in ("Tak", "tak", "TAK"):
    print("Uniwersytet Warszawski", "Uniwesrsytet Wroclawski UWr", "Uniwersytet Krakowski Jagiellońskiego")
    b = str(input('Podaj Imię:'))
    nowy_st.append(b)
    b1 = str(input('Podaj Nazwisko:'))
    nowy_st.append(b1)
    b2 = str(input('Podaj Datę urodzenia:'))
    nowy_st.append(b2)
    while True:
        b3 = str(input('Podaj Wydzial:'))
        if b3 in wydz:
            nowy_st.append(b3)
            try:
                with open('st.json', 'r') as plik:
                    st = json.load(plik)
            except FileNotFoundError:
                st = {}
            while True:
                k = str(input('Podaj uniwersytet'))
                if poprawnosc(uni1) == poprawnosc(k):
                    st['Uniwersytet Warszawski'] = nowy_st
                    with open('st.json', 'w') as plik:
                        json.dump(st, plik, indent=4)
                        print("Dziekuje ze skorzystales z naszego dziennika! Twoje dane zostaly zapisane.")
                        print(nowy_st)
                        break


                elif poprawnosc(uni2) == poprawnosc(k):
                    st['Uniwesrsytet Wroclawski UWr'] = nowy_st
                    with open('st.json', 'w') as plik:
                        json.dump(st, plik, indent=4)
                        print("Dziekuje ze skorzystales z naszego dziennika!Twoje dane zostaly zapisane.")
                        print(nowy_st)
                        break



                elif poprawnosc(uni3) == poprawnosc(k):
                    st['Uniwersytet Krakowski Jagiellońskiego'] = nowy_st
                    with open('st.json', 'w') as plik:
                        json.dump(st, plik, indent=4)
                        print("Dziekuje ze skorzystales z naszego dziennika!Twoje dane zostaly zapisane.")
                        print(nowy_st)
                        break

                else:
                    if poprawnosc(uni1) != poprawnosc(k):
                        print("Nie ma takiego uniwersytetu. Sprobuj ponownie.")

        else:
            print("Nie ma takiego wydzialu,sprobuj ponownie.")

else:
    print("Dziekuje ze skorzystales z naszego dziennika!")


