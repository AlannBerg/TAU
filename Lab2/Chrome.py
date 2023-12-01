from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging
import time
from selenium.common.exceptions import TimeoutException


logger = logging.getLogger('s22433')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Chrome()

try:
    
    # Test 1: Kliknięcie w odpowiedni link"
    logger.info('Klikam w link A/B Testing')
    driver.get("https://the-internet.herokuapp.com/")
    temp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.LINK_TEXT, "A/B Testing"))))
    temp.click()
    time.sleep(2)
    print("Test 1 Passed")

    # Test 2: Powrót do strony głównej. Dodanie elementu"
    logger.info('Wracam do strony głównej. Dodam element przyciskając przycisk')
    driver.back()
    temp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.LINK_TEXT, "Add/Remove Elements"))))
    temp.click()
    temp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "//button[text()='Add Element']"))))
    temp.click()
    try:
        # Try to find the div   element
        div_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.CLASS_NAME, "added-manually"))))
        logger.info('Dodano element poprawnie')
    except NoSuchElementException:
        # Handle the case where the div element is not found
        logger.error('Element nie dodał się poprawnie')

    time.sleep(2)
    print("Test 2 Passed")


    # Test 3: Usuniecie dodanego elementu"
    logger.info('Usuwam dodany element')
    div_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.CLASS_NAME, "added-manually"))))
    div_element.click()
    try:
        WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.CLASS_NAME, "added-manually")))
        logger.info('Element został poprawnie usuniety')
    except TimeoutException:
        logger.error('Błąd podczas usuwania elementu')
    time.sleep(2)
    print("Test 3 Passed")

    #Test 4: Zaznaczenie checkboxa
    logger.info('Zaznaczenie checkboxa')
    driver.back()
    temp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.LINK_TEXT, "Checkboxes"))))
    temp.click()

    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
    checkbox.click()
  
    time.sleep(2)
    print("Test 4 Passed")


except Exception as e:
    logger.error(f'Test failed: {str(e)}')

finally:
    time.sleep(2)
    driver.close()