# Nazwa pliku do importu i lista adresów do usunięcia [cite: 68, 67]
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

def update_file(import_file, remove_list):
    # Otwarcie pliku w trybie odczytu [cite: 11, 71]
    with open(import_file, "r") as file:
        # Odczytanie zawartości i zapisanie jako ciąg znaków [cite: 18, 75]
        ip_addresses = file.read()

    # Konwersja ciągu znaków na listę (split) [cite: 25, 79]
    ip_addresses = ip_addresses.split()

    # Iteracja przez listę adresów IP [cite: 32, 80]
    for element in ip_addresses:
        # Sprawdzenie, czy dany adres znajduje się na liście do usunięcia [cite: 33, 81]
        if element in remove_list:
            # Usunięcie adresu z listy [cite: 38, 82]
            ip_addresses.remove(element)

    # Ponowna konwersja listy na ciąg znaków (join) [cite: 41, 83]
    ip_addresses = " ".join(ip_addresses)

    # Nadpisanie pliku zaktualizowaną listą [cite: 47, 84, 85]
    with open(import_file, "w") as file:
        file.write(ip_addresses)

# Wywołanie funkcji [cite: 50, 87]
update_file(import_file, remove_list)
