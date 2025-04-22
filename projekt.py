import json


print("Witamy w dzienniku studentów!")
print('Jakie są wydziały:')
#dane: kierunki sdudiow

k_st = {
    "Uniwersytet Warszawski": ["Wydział Archeologii","Wydział Biologii",
    "Wydział Chemii","Wydział Dziennikarstwa, Informacji i Bibliologii","Wydział Medyczny"],
    "Uniwesrsytet Wroclawski UWr": ["Wydział Komunikacji Społecznej i Mediów","Wydział Matematyki i Informatyki","Wydział Nauk Biologicznych",
                                "Wydział Nauk Historycznych i Pedagogicznych", "Wydział Nauk Społecznych"],
    "Uniwersytet Krakowski Jagiellońskiego": ["Wydział Biochemii, Biofizyki i Biotechnologii","Wydział Biologii","Wydział Fizyki, Astronomii i Informatyki Stosowanej",
                              "Wydział Matematyki i Informatyki"]

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

#wyswietlanie danych z pliku json

with open("k_st.json", "r", encoding="utf-8") as plik:
    k_st = json.load(plik)
    for key, wartosc in k_st.items():
        print(f"{key}: {wartosc}")
#Zapisywanie danych studentow do pliku typu json
with open("k_st.json", "w", encoding="utf-8") as f:
    json.dump(st, f, ensure_ascii=False, indent=4)

#wyswietlanie danych z pliku json
with open("st.json", "r", encoding="utf-8") as f:
    st = json.load(f)
    for key, wartosc in st.items():
        print(f"{key}: {wartosc}")


#wprowadzanie nowych dannych o nowym studencie
nowy_st = []

a = str(input('Czy chcesz wprowadzic nowe dane?:'))
print("Uniwersytet Warszawski","Uniwesrsytet Wroclawski UWr","Uniwersytet Krakowski Jagiellońskiego")
if a == "Tak" or 'tak':
    b = str(input('Podaj Imię:'))
    nowy_st.append(b)
    b1 = str(input('Podaj Nazwisko:'))
    nowy_st.append(b1)
    b2 = str(input('Podaj Datę urodzenia:'))
    nowy_st.append(b2)
    b3 = str(input('Podaj Wydzial:'))
    nowy_st.append(b3)

print(nowy_st)

try:
    with open('st.json', 'r') as plik:
        st = json.load(plik)
except FileNotFoundError:
    st = {}
k = str(input('Podaj uniwersytet'))
if k == "Uniwersytet Warszawski":
    st['Uniwersytet Warszawski'] = nowy_st
    with open('st.json', 'w') as plik:
        json.dump(st, plik, indent=4)

if k == "Uniwesrsytet Wroclawski UWr":
    st['Uniwesrsytet Wroclawski UWr'] = nowy_st
    with open('st.json', 'w') as plik:
        json.dump(st, plik, indent=4)

if k == "Uniwersytet Krakowski Jagiellońskiego":
    st['Uniwersytet Krakowski Jagiellońskiego'] = nowy_st
    with open('st.json', 'w') as plik:
        json.dump(st, plik, indent=4)

