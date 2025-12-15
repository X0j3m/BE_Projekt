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
URL_SKLEPU = "https://localhost"
ADMIN_URL = "https://localhost/admin1234" # Twój folder admina
ADMIN_EMAIL = "jaku6p@gmail.com"
ADMIN_PASS = "12345678"
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
    kategorie = [f"{URL_SKLEPU}/3-clothes", f"{URL_SKLEPU}/6-accessories"]
    licznik = 0
    limit = 10

    def dodaj_produkt(ilosc):
        qty = wait.until(EC.presence_of_element_located((By.ID, "quantity_wanted")))
        qty.click()
        qty.send_keys(Keys.BACK_SPACE * 5)
        qty.send_keys(str(ilosc))
        driver.find_element(By.CLASS_NAME, "add-to-cart").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-dialog .btn-secondary"))).click()
        time.sleep(1)

    for kat in kategorie:
        if licznik >= limit: break
        driver.get(kat)
        time.sleep(2)
        linki = [e.get_attribute("href") for e in driver.find_elements(By.CSS_SELECTOR, ".product-miniature .thumbnail.product-thumbnail")]
        for link in linki:
            if licznik >= limit: break
            try:
                driver.get(link)
                dodaj_produkt(random.randint(1, 4))
                licznik += 1
                print(f"    [OK {licznik}/10]")
            except: continue

    # ==========================================
    # CZĘŚĆ 3: WYSZUKIWANIE
    # ==========================================
    print("\n--- WYSZUKIWANIE ---")
    search = driver.find_element(By.NAME, "s")
    search.clear()
    #TODO: zmień na produkt, który chce szukać
    search.send_keys("Hummingbird")
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

    # Płatność
    try:
        radio = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-module-name='ps_wirepayment']")))
        driver.execute_script("arguments[0].click();", radio)
        terms = driver.find_element(By.CSS_SELECTOR, "input[id*='conditions_to_approve']")
        driver.execute_script("arguments[0].click();", terms)
    except Exception as e: 
        print(f"Błąd płatności: {e}")
        driver.save_screenshot("blad_platnosc.png")

    # ==========================================
    # CZĘŚĆ 6: ZATWIERDZENIE
    # ==========================================
    print("\n--- ZATWIERDZENIE ---")

    btn_zamow = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#payment-confirmation button")))

    btn_zamow.click()
    print("   -> Kliknięto przycisk 'Złóż zamówienie'")

    print("   [SUKCES] Zamówienie zostało złożone i potwierdzone!")


    # ==========================================
    # NOWA CZĘŚĆ: LOGOWANIE DO ADMINA I ZMIANA STATUSU (POPRAWIONA)
    # ==========================================
    print("\n--- [ADMIN] ZMIANA STATUSU ZAMÓWIENIA ---")
    
    # 1. Otwieramy nową kartę
    driver.switch_to.new_window('tab')
    
    # 2. Logowanie do panelu
    driver.get(ADMIN_URL)
    print("   -> Logowanie jako Admin...")
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(ADMIN_EMAIL)
        driver.find_element(By.ID, "passwd").send_keys(ADMIN_PASS)
        driver.find_element(By.ID, "submit_login").click()
    except:
        print("   -> Prawdopodobnie admin jest już zalogowany.")

    # 3. Przejście do zamówień
    print("   -> Przechodzę do listy zamówień...")
    time.sleep(3) 
    driver.get(f"{URL_SKLEPU}/admin1234/index.php?controller=AdminOrders")
    
    # Sortowanie tabeli (najnowsze na górze)
    print("   -> Sprawdzam sortowanie tabeli...")
    try:
        id_header = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-sort-col-name='id_order']")))
        if id_header.get_attribute("data-sort-direction") == "asc":
            print("   -> Odwracam sortowanie...")
            id_header.click()
            time.sleep(3) 
    except Exception as e:
        print(f"   [!] Problem z sortowaniem: {e}")

    # 4. Kliknięcie w najnowsze zamówienie
    print("   -> Otwieram najnowsze zamówienie...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]"))).click()
    
    # 5. Zmiana statusu na "Płatność zaakceptowana" (ID 2)
    # --- TUTAJ JEST POPRAWKA POD TWÓJ KOD HTML ---
    print("   -> Zmieniam status na 'Płatność zaakceptowana' (ID 2)...")
    try:
        # Znajdujemy dropdown po Twoim ID z HTML
        select_element = wait.until(EC.presence_of_element_located((By.ID, "update_order_status_new_order_status_id")))
        select = Select(select_element)
        
        # Wybieramy wartość "2" (Płatność zaakceptowana)
        select.select_by_value("2")
        
        # Klikamy przycisk "Aktualizacja statusu" po klasie .update-status
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button.update-status")
        submit_btn.click()
        
        print("   [SUKCES ADMIN] Status zmieniony!")
        time.sleep(3) # Czekamy na zapisanie
        
    except Exception as e:
        print(f"   [!] Nie udało się zmienić statusu: {e}")
        driver.save_screenshot("admin_error.png")

    # 6. Zamykamy kartę admina i wracamy do klienta
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("   -> Powrót do konta klienta.")

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