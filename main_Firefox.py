from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
import time

# Variables
COLOR = "#C12F2F"  # Representación de color en formato hexadecimal
DATA = "2024-11-20"  
DATETIME = "2024-11-20T00:00"  
EMAIL = "yo@mail.com"
MONTH = "mayo"
YEAR = "2024"  # Si no se pone el mes y el año por separado, tira error
NUMBER = "44"

def main():
    service = Service(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    

    driver = webdriver.Firefox(service=service, options=options)
    try:
        # Navegar a la página a testear
        driver.get("https://testpages.eviltester.com/styled/html5-form-test.html")

        # Esperas explícitas para asegurar que los elementos estén disponibles
        pick_a_color = Wait(driver, 10).until(EC.visibility_of_element_located((By.ID, "colour-picker")))
        pick_a_color.clear()
        pick_a_color.send_keys(COLOR)

        pick_a_date = Wait(driver, 10).until(EC.visibility_of_element_located((By.ID, "date-picker")))
        pick_a_date.clear()
        pick_a_date.send_keys(DATA)

        pick_a_datetime = Wait(driver, 10).until(EC.visibility_of_element_located((By.ID, "date-time-picker")))
        pick_a_datetime.clear()
        pick_a_datetime.send_keys(DATETIME)

        insert_email = Wait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email-field")))
        insert_email.clear()  # Limpiar el campo antes de enviar el nuevo valor
        insert_email.send_keys(EMAIL)

        pick_a_month = Wait(driver, 10).until(EC.visibility_of_element_located((By.ID, "month-field")))
        pick_a_month.clear()
        pick_a_month.send_keys(MONTH)
        pick_a_month.send_keys(Keys.TAB)
        pick_a_month.send_keys(YEAR)

        pick_a_number = Wait(driver, 10).until(EC.visibility_of_element_located((By.ID, "number-field")))
        pick_a_number.clear()
        pick_a_number.send_keys(NUMBER)

        # Hacer clic en el botón de envío
        submit_button = Wait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.styled-click-button[type='submit']")))
        submit_button.click()

        # Esperar un poco para ver el resultado
        time.sleep(20)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
