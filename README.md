# Projek na przedmiot Biznes Elektroniczny
# Projekt sklepu https://pancernik.eu/

# Skład zespołu
Kurpiewski      Paweł       198203
Pastuszka       Jakub       198339
Ptasznik        Michał      197933
Pytka           Ryszard     198323

## Opis projektu
Projekt przedstawia wdrożenie sklepu internetowego opartego o **PrestaShop 1.7.8**, uruchamianego w środowisku **Docker Compose**.  
System został rozszerzony o własne modyfikacje HTML/PHP, testy automatyczne oraz narzędzie do scrapowania danych produktowych.

## 🚀 Zawartość projektu

| Serwis | Opis | Port |
|--------|------|------|
| 🗄️ **MariaDB** | baza danych sklepu | `3306` |
| 🧠 **Adminer** | prosty panel do zarządzania bazą danych | `8081` |
| 🛒 **PrestaShop** | właściwy sklep internetowy | `8080` |

## ⚙️ Wykorzystane technologie
- **PrestaShop**
- **PHP**
- **MariaDB**
- **Docker Compose**

## Wymaganne technologie - Scraper
- **python 3.10.12**
- **scrapy 2.13.4**
- **scrapy_playwright 0.0.44**
- **playwright 1.56.0**
- **itemadapter 0.12.2**
- **Requests 2.32.5**
## Włączenie projektu 
- wchodzimy w terminalu w folder, w którym znajduje się repozytorium
- używamy komendy 'docker compose up -d' w celu włączeniu kontenera
- wchodzimy na 'localhost:8080' - miejsce gdzie znajduje się prestashop
- w celu przegądania bazy danych można wejść na 'localhost:8081' - włącza się adminer za pomocą, którego można modyfikować baze


# Zapisanie pracy w adminie

zapisanie backupu
```bash
docker exec -i mariadb mysqldump -u root -proot prestashop > prestashop.sql
```