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
#options.add_argument("--headless")                        # działanie w tle


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10) # Maksymalny czas oczekiwania na element

try:
    print("--- REJESTRACJA ---")
    driver.get(f"{URL_SKLEPU}/logowanie?create_account=1%20data-link-action=")


    # Wypełnianie danych
    imie = FAKER.first_name()
    nazwisko = FAKER.last_name()
    email = FAKER.email()
    haslo = "Haslo1234!"

    print("--- KROK 1: Wypełnianie danych e-mail, haslo ---")
    #driver.find_element(By.NAME, "firstname").send_keys(imie)
    #driver.find_element(By.NAME, "lastname").send_keys(nazwisko)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(haslo)
    driver.find_element(By.ID, "field-password-confirm").send_keys(haslo)
    

    print("--- KROK 2: Zgody ---")
    # Zgody (szukamy wszystkich wymaganych checkboxów)
    checkboxy = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    for checkbox in checkboxy:
        if not checkbox.is_selected():
            checkbox.click()

    print("--- KROK 3: Zapisz ---")
    # Kliknij Zapisz
    driver.find_element(By.CLASS_NAME, "btn-register-dark").click()

    print("--- WERYFIKACJA REJESTRACJI I LOGOWANIA ---")
    link_naglowka = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='moje-konto']")))
    
    print("Klikam w link w nagłówku...")
    link_naglowka.click()

    # 2. Poczekaj na zmianę URL i pobierz go
    time.sleep(2) # Krótka pauza na przeładowanie strony
    aktualny_url = driver.current_url
    
    print(f"Adres po kliknięciu: {aktualny_url}")

    # 3. Logika testu: Czy jesteśmy na koncie, czy na logowaniu?
    if "controller=my-account" in aktualny_url or "/moje-konto" in aktualny_url:
        # Dodatkowy warunek: NIE może być "login" ani "back=" w adresie
        if "login" not in aktualny_url and "back=" not in aktualny_url:
            print(f"SUKCES: Użytkownik jest zalogowany (URL to moje-konto).")
        else:
             raise Exception("BŁĄD: URL zawiera 'moje-konto', ale wygląda na przekierowanie do logowania.")
    else:
        # Jeśli URL to np. .../logowanie?back=my-account
        raise Exception("BŁĄD: Kliknięcie przeniosło do logowania zamiast do konta. Rejestracja nie zalogowała użytkownika.")

except Exception as e:
    print(f"BŁĄD: {e}")
finally:
    driver.quit()