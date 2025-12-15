import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

# --- KONFIGURACJA ---
URL_SKLEPU = "https://localhost"
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
    driver.get(f"{URL_SKLEPU}/logowanie?create_account=1") # Poprawiłem URL na czystszy

    # Wypełnianie danych
    imie = FAKER.first_name()
    nazwisko = FAKER.last_name()
    email = FAKER.email()
    haslo = "Haslo1234!"

    print("--- Wypełnianie danych e-mail, haslo ---")
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(haslo)
    
    # Obsługa potwierdzenia hasła (w try, bo może go nie być w zależności od wersji)
    try:
        driver.find_element(By.ID, "field-password-confirm").send_keys(haslo)
    except:
        pass

    print("--- Zgody ---")
    checkboxy = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    for checkbox in checkboxy:
        if not checkbox.is_selected():
            # Używamy JS click, bo czasem elementy są zasłonięte
            driver.execute_script("arguments[0].click();", checkbox)

    print("--- Zapisz ---")
    driver.find_element(By.CLASS_NAME, "btn-register-dark").click()

    print("--- WERYFIKACJA REJESTRACJI I LOGOWANIA ---")
    # Klikamy w link prowadzący do konta
    link_naglowka = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='moje-konto']")))
    link_naglowka.click()

    # Poczekaj na zmianę URL
    time.sleep(2)
    aktualny_url = driver.current_url

    # Sprawdzamy czy nas nie wylogowało
    if "controller=my-account" in aktualny_url or "/moje-konto" in aktualny_url:
        if "login" not in aktualny_url and "back=" not in aktualny_url:
            print(f"[SUKCES]: Użytkownik jest zalogowany.")
        else:
             raise Exception("[BŁĄD]: URL zawiera 'moje-konto', ale wygląda na przekierowanie do logowania.")
    else:
        raise Exception("[BŁĄD]: Kliknięcie przeniosło do logowania zamiast do konta.")

    # ==========================================
    # CZĘŚĆ 2: DODAWANIE PRODUKTÓW
    # ==========================================
    print("\n--- DODAWANIE 10 PRODUKTÓW DO KOSZYKA ---")

    #[TODO] Zmodyfikuj kategorie na takie, które są w naszym sklepie
    kategorie = [
        f"{URL_SKLEPU}/3-clothes",      # Sprawdź czy ID kategorii są poprawne!
        f"{URL_SKLEPU}/6-accessories"
    ]

    licznik_produktow = 0
    limit_produktow = 10

    # Definicja funkcji wewnątrz (lub może być na zewnątrz, byle wywołana tutaj)
    def dodaj_pojedynczy_produkt(driver, wait, ilosc):
        print(f"   -> Ustawienie ilości: {ilosc}")
        qty_input = wait.until(EC.presence_of_element_located((By.ID, "quantity_wanted")))
        qty_input.click()
        qty_input.send_keys(Keys.BACK_SPACE * 5)
        qty_input.send_keys(str(ilosc))

        print("   -> Kliknięcie Dodaj")
        add_btn = driver.find_element(By.CLASS_NAME, "add-to-cart")
        add_btn.click()

        print("   -> Zamykanie okienka (modal)")
        continue_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-dialog .btn-secondary")))
        continue_btn.click()
        time.sleep(1) # Krótki oddech dla przeglądarki

    # Pętla po kategoriach
    for url_kategorii in kategorie:
        if licznik_produktow >= limit_produktow:
            break
            
        print(f"--> Wchodzę do kategorii: {url_kategorii}")
        driver.get(url_kategorii)

        print("    Pobieranie linków...")
        time.sleep(2)
        miniaturki = driver.find_elements(By.CSS_SELECTOR, ".product-miniature .thumbnail.product-thumbnail")
        # Pobieramy same linki tekstowe, żeby nie tracić referencji do elementów po przeładowaniu strony
        linki_produktow = [elem.get_attribute("href") for elem in miniaturki]

        for link in linki_produktow:
            if licznik_produktow >= limit_produktow:
                break
            
            try:
                driver.get(link)
                ilosc = random.randint(1, 4)
                dodaj_pojedynczy_produkt(driver, wait, ilosc)
                
                licznik_produktow += 1
                print(f"    [SUKCES {licznik_produktow}/10] Dodano produkt.")
                
            except Exception as e:
                print(f"    [!] Błąd przy produkcie: {e}")
                continue

    print(f"\n[KONIEC] Pomyślnie dodano {licznik_produktow} produktów.")

except Exception as e:
    print(f"\n[BŁĄD KRYTYCZNY CAŁEGO TESTU]: {e}")
    driver.save_screenshot("blad_krytyczny.png")

finally:
    print("Zamykanie przeglądarki...")
    driver.quit()