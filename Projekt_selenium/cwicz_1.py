first_name = " jan "
last_name = "kowalski"
full_name = f"{first_name.strip()} {last_name}"
print(full_name.title())
print(full_name.upper())
print(full_name.lower())
message = f"Witaj, {full_name.title()}!"
print(message)

samochod = "Ford"
typ = "Mustang"
tekst = f"{samochod} {typ}"
print(tekst)

name = "Iwona"
surname = "Białek"
adres = "Konwaliowa 3"
kod = "01-003 Białystok"

#użycie znaków: 1.przenoszenie do nowej linii \n oraz 2.tabulator \t
full_data = f"{name} {surname}\n\t{adres}\n\t{kod}"
print(full_data)
print(f"Witaj,{name}! Czy chcesz dzisiaj poznawać Pythona?")

#pomijanie białych znaków: /
#lstrip - kasuje tabulatory,/
# rstrip - kasuje spacje i podział linii/
#strip - kasuje wszystko
famous_person = "\t Albert Einstein \n"
print(f'{famous_person.strip()} powiedział kiedyś: \
"Osoba, która nigdy nie popełniła błędu,\njest kimś,\
 kto nigdy nie próbował nieczego nowego"')
