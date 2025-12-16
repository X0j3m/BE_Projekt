# 🛒 Automatyzacja Testów E2E - PrestaShop (Selenium & Python)

Projekt zawiera skrypt w języku Python, który przeprowadza kompleksowy, automatyczny test sklepu internetowego opartego na silniku PrestaShop. Skrypt symuluje pełną ścieżkę zakupową klienta oraz wykonuje czynności administracyjne.

## 📋 Scenariusz testowy

Skrypt automatycznie realizuje następujące kroki:

1.  **Rejestracja i Logowanie:**
    * Tworzy nowe konto klienta przy użyciu losowych danych (biblioteka `Faker`).
    * Weryfikuje poprawne zalogowanie.
2.  **Dodawanie produktów:**
    * Wchodzi w kategorie *Clothes* oraz *Accessories*.
    * Dodaje do koszyka 10 produktów w losowych ilościach.
    * Obsługuje okna modalne (pop-upy) po dodaniu produktu.
3.  **Wyszukiwanie:**
    * Wpisuje frazę "Hummingbird" w wyszukiwarkę.
    * Losuje jeden produkt z wyników i dodaje go do koszyka.
4.  **Edycja koszyka:**
    * Przechodzi do koszyka.
    * Usuwa 3 pozycje z listy.
5.  **Proces zakupu (Checkout):**
    * Uzupełnia adres dostawy (jeśli wymagane).
    * Wybiera przewoźnika.
    * Wybiera płatność **Przelewem bankowym** (szuka słów kluczowych *Bank/Wire/Przelew*).
    * Zatwierdza regulamin i składa zamówienie.
6.  **Panel Administratora (Nowa karta):**
    * Otwiera nową kartę w przeglądarce.
    * Loguje się do panelu Admina PrestaShop.
    * Znajduje ostatnie zamówienie (automatycznie sortuje tabelę od najnowszych).
    * Zmienia status zamówienia na **"Płatność zaakceptowana"** (ID 2).
7.  **Pobranie faktury:**
    * Wraca do karty klienta.
    * Wchodzi w historię zamówień.
    * Pobiera wygenerowaną fakturę VAT (PDF).

## ⚙️ Wymagania

* **Python 3.8+**
* Przeglądarka **Google Chrome**
* Dostęp do sklepu PrestaShop (lokalnie lub na serwerze testowym)

## 🚀 Instalacja i Uruchomienie

### 1. Pobranie projektu
Pobierz pliki projektu do wybranego folderu.

### 2. Konfiguracja wirtualnego środowiska (Zalecane)
Aby zachować porządek w bibliotekach, utwórz wirtualne środowisko.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**bash**
```bash
pip install selenium webdriver-manager faker
```