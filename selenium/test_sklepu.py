import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select # Potrzebne do zmiany statusu
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

# --- KONFIGURACJA ---
URL_SKLEPU = "https://localhost:19793"
ADMIN_URL = "https://localhost:19793/admin1234" # Twój folder admina
FAKER = Faker("pl_PL")

# Ustawienia przeglądarki
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
options.add_argument("--window-size=1920,1080")
# options.add_argument("--headless") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

try:
    # ==========================================
    # CZĘŚĆ 1: REJESTRACJA I LOGOWANIE
    # ==========================================
    print("--- REJESTRACJA ---")
    driver.get(f"{URL_SKLEPU}/logowanie?create_account=1") 

    imie = FAKER.first_name()
    nazwisko = FAKER.last_name()
    email = FAKER.email()
    haslo = "Haslo1234!"

    print("--- Wypełnianie danych ---")
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(haslo)
    try:
        driver.find_element(By.ID, "field-password-confirm").send_keys(haslo)
    except:
        pass

    print("--- Zgody ---")
    checkboxy = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    for checkbox in checkboxy:
        if not checkbox.is_selected():
            driver.execute_script("arguments[0].click();", checkbox)

    print("--- Zapisz ---")
    driver.find_element(By.CLASS_NAME, "btn-register-dark").click()

    print("--- WERYFIKACJA ---")
    link_naglowka = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='moje-konto']")))
    link_naglowka.click()

    time.sleep(2)
    aktualny_url = driver.current_url

    if "controller=my-account" in aktualny_url or "/moje-konto" in aktualny_url:
        if "login" not in aktualny_url and "back=" not in aktualny_url:
            print(f"[SUKCES]: Zalogowano.")
        else:
             raise Exception("Błąd logowania (URL).")
    else:
        raise Exception("Błąd przekierowania.")

    # ==========================================
    # CZĘŚĆ 2: DODAWANIE PRODUKTÓW
    # ==========================================
    print("\n--- DODAWANIE PRODUKTÓW ---")
    #TODO: zmień kategorie na swoje
    kategorie = [f"{URL_SKLEPU}/4-do-smartfona", f"{URL_SKLEPU}/6-do-tabletu"]
    licznik = 0
    limit = 10

    def dodaj_produkt(chciana_ilosc):
        try:
            btn_add = driver.find_element(By.CLASS_NAME, "add-to-cart")
            if not btn_add.is_enabled():
                print("    [POMINIĘTO]: Przycisk zakupu jest nieaktywny (brak towaru).")
                return False
                
            try:
                element_stanu = driver.find_element(By.CSS_SELECTOR, ".product-quantities span")
                dostepna_ilosc = int(element_stanu.get_attribute("data-stock"))
            except:
                # Jeśli nie ma elementu ze stanem, a przycisk był aktywny (mało prawdopodobne, ale możliwe)
                # ustawiamy np. 1 lub sprawdzamy komunikat o braku
                print("    [INFO]: Nie znaleziono licznika sztuk, sprawdzam dostępność...")
                return False
                        
            ilosc_do_dodania = min(chciana_ilosc, dostepna_ilosc)            
            print(f"    [MAGAZYN]: Dostępnych: {dostepna_ilosc}, Chcemy: {chciana_ilosc}, Bierzemy: {ilosc_do_dodania}")
            
            # 2. Logika wyboru mniejszej wartości
            ilosc_do_dodania = min(chciana_ilosc, dostepna_ilosc)
            
            if ilosc_do_dodania <= 0:
                print("    [POMINIĘTO]: Brak towaru w magazynie.")
                return False

            # 3. Wpisanie ilości
            qty = driver.find_element(By.ID, "quantity_wanted")
            qty.click()
            qty.send_keys(Keys.CONTROL + "a") # Zaznacz wszystko
            qty.send_keys(Keys.BACKSPACE)    # Usuń
            qty.send_keys(str(ilosc_do_dodania))
            
            # 4. Dodanie do koszyka
            driver.find_element(By.CLASS_NAME, "add-to-cart").click()
            
            # Czekamy na popup i zamykamy go
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-dialog .btn-secondary"))).click()
            time.sleep(1)
            return True
        except Exception as e:
            print(f"    [BŁĄD DODAWANIA]: {e}")
            return False

    # Główna pętla losowania
    while licznik < limit:
        # 1. Losujemy kategorię
        kat_url = random.choice(kategorie)
        driver.get(kat_url)
        time.sleep(2)

        while licznik < limit:
            # 2. Pobieramy wszystkie linki do produktów na AKTUALNEJ stronie
            produkty = driver.find_elements(By.CSS_SELECTOR, ".product-miniature .thumbnail.product-thumbnail")
            
            if not produkty:
                break # Wyjdź do losowania innej kategorii, jeśli pusta

            # 3. Wybieramy losowy produkt z tej strony
            losowy_produkt = random.choice(produkty)
            link_produktu = losowy_produkt.get_attribute("href")
            
            driver.get(link_produktu)
            if dodaj_produkt(random.randint(1, 3)):
                licznik += 1
                print(f"    [OK {licznik}/{limit}] Dodano: {link_produktu}")
            
            if licznik >= limit: break

            # --- LOGIKA PAGINACJI ---
            driver.get(kat_url) # Powrót do listy produktów w kategorii
            time.sleep(1)
            
            try:
                # Szukamy przycisku "Następny" (zazwyczaj klasa .next lub link z rel="next")
                next_page = driver.find_elements(By.CSS_SELECTOR, "a.next, .pagination a[rel='next']")
                
                if next_page and next_page[0].is_displayed():
                    print("   [PAGINACJA]: Przechodzę na kolejną stronę...")
                    kat_url = next_page[0].get_attribute("href")
                    driver.get(kat_url)
                    time.sleep(2)
                else:
                    print("   [INFO]: To ostatnia strona tej kategorii.")
                    break # Brak kolejnych stron, wylosuj nową kategorię
            except Exception as e:
                print(f"   [INFO]: Koniec stron w tej kategorii lub błąd: {e}")
                break
    # ==========================================
    # CZĘŚĆ 3: WYSZUKIWANIE
    # ==========================================
    print("\n--- WYSZUKIWANIE ---")
    search = driver.find_element(By.NAME, "s")
    search.clear()
    #TODO: zmień na produkt, który chce szukać
    search.send_keys("samsung")
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    wyniki = driver.find_elements(By.CSS_SELECTOR, ".product-miniature .thumbnail.product-thumbnail")
    if wyniki:
        driver.get(wyniki[0].get_attribute("href"))
        dodaj_produkt(1)
        print("   [SUKCES] Dodano z wyszukiwania.")

    # ==========================================
    # CZĘŚĆ 4: USUWANIE
    # ==========================================
    print("\n--- USUWANIE Z KOSZYKA ---")
    driver.get(f"{URL_SKLEPU}/index.php?controller=cart&action=show")
    time.sleep(2)
    for _ in range(3):
        try:
            kosze = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "remove-from-cart")))
            if kosze:
                kosze[0].click()
                time.sleep(2)
            else: break
        except: break

    # ==========================================
    # CZĘŚĆ 5: CHECKOUT
    # ==========================================
    print("\n--- CHECKOUT ---")
    driver.get(f"{URL_SKLEPU}/zamówienie")
    time.sleep(2)

    # Adres
    try:
        wait.until(EC.presence_of_element_located((By.ID, "checkout-addresses-step")))
        pola = driver.find_elements(By.NAME, "address1")
        if len(pola) > 0 and pola[0].is_displayed():
            driver.find_element(By.NAME, "address1").send_keys("Ulica Testowa 15")
            driver.find_element(By.NAME, "postcode").send_keys("00-950")
            driver.find_element(By.NAME, "city").send_keys("Warszawa")
            driver.find_element(By.NAME, "confirm-addresses").click()
        else:
             # Kliknij dalej jeśli adres już jest
             btns = driver.find_elements(By.NAME, "confirm-addresses")
             if btns and btns[0].is_displayed(): btns[0].click()
        time.sleep(2)
    except Exception as e: print(f"Info adres: {e}")

    # Dostawa
    try:
        wait.until(EC.element_to_be_clickable((By.NAME, "confirmDeliveryOption"))).click()
        time.sleep(2)
    except: pass

    # --- PŁATNOŚĆ (WYBÓR KARTY) ---
    print("    -> Wybieram płatność kartą...")
    try:
        # 1. Znalezienie i kliknięcie opcji płatności kartą
        # Selektor po ID, który jest unikalny dla karty w Twoim HTML
        opcja_karta = wait.until(EC.presence_of_element_located((By.ID, "payment-option-2")))
        driver.execute_script("arguments[0].click();", opcja_karta)
        
        # 2. Wypełnienie danych karty (opcjonalnie, jeśli pola są widoczne)
        # Pola te pojawiają się w sekcji #pay-with-payment-option-2-form po wybraniu radiobuttona
        time.sleep(1) # Chwila na rozwinięcie formularza
        
        driver.find_element(By.NAME, "card_number").send_keys("4242 4242 4242 4242")
        driver.find_element(By.NAME, "card_expiry").send_keys("12/26")
        driver.find_element(By.NAME, "card_cvv").send_keys("123")
        driver.find_element(By.NAME, "card_holder").send_keys(f"{imie} {nazwisko}")

        # 3. Akceptacja regulaminu
        # Selektor dopasowany do Twojego ID: conditions_to_approve[terms-and-conditions]
        regulamin = driver.find_element(By.CSS_SELECTOR, "input[id*='conditions_to_approve']")
        if not regulamin.is_selected():
            driver.execute_script("arguments[0].click();", regulamin)
            
        print("    [SUKCES] Dane karty uzupełnione.")
    except Exception as e:
        print(f"    [BŁĄD PŁATNOŚCI KARTĄ]: {e}")

    # ==========================================
    # CZĘŚĆ 6: ZATWIERDZENIE
    # ==========================================
    print("\n--- ZATWIERDZENIE ---")

    btn_zamow = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#payment-confirmation button")))

    btn_zamow.click()
    print("   -> Kliknięto przycisk 'Złóż zamówienie'")

    print("   [SUKCES] Zamówienie zostało złożone i potwierdzone!")


    # ==========================================
    # CZĘŚĆ 7 i 8: POBRANIE FAKTURY
    # ==========================================
    print("\n--- STATUS I FAKTURA ---")
    
    # Wchodzimy w historię zamówień
    driver.get(f"{URL_SKLEPU}/historia-zamowien")
    
    try:
        # Czekamy na tabelę
        wait.until(EC.presence_of_element_located((By.ID, "content")))
        
        # 1. Wyświetlenie statusu (z pierwszego wiersza)
        try:
            # Szukamy etykiety statusu (zazwyczaj klasa label-pill lub podobna w kolumnie statusu)
            status_element = driver.find_element(By.CSS_SELECTOR, "tbody tr:first-child .label-pill")
            print(f"   [STATUS ZAMÓWIENIA]: {status_element.text}")
        except:
            print("   [INFO] Nie udało się odczytać tekstu statusu.")

        # 2. Pobranie faktury
        linki_faktur = driver.find_elements(By.CSS_SELECTOR, "a[href*='pdf-invoice']")
        
        if len(linki_faktur) > 0:
            link_do_faktury = linki_faktur[0]
            print(f"   [SUKCES] Faktura dostępna. Klikam, aby pobrać...")
            
            # --- KLUCZOWE: KLIKNIĘCIE ---
            link_do_faktury.click()
            
            print("   -> Rozpoczęto pobieranie pliku PDF.")
            time.sleep(5) # Czekamy chwilę, żeby plik zdążył się pobrać przed zamknięciem przeglądarki
        else:
            print("   [BŁĄD] Faktura nadal niedostępna!")
            
    except Exception as e:
        print(f"   [!] Błąd w sekcji historii: {e}")

    print("\n##############################################")
    print("   TEST ZAKOŃCZONY POMYŚLNIE")
    print("##############################################")

except Exception as e:
    print(f"\n[BŁĄD KRYTYCZNY]: {e}")
    driver.save_screenshot("blad_krytyczny.png")

finally:
    # driver.quit() # Zakomentowane, żebyś widział wynik
    pass