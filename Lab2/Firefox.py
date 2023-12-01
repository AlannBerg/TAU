from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

logger = logging.getLogger('s22203')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Firefox()

try:
    # Test 1
    logger.info('Przechodzę na stronę selenium')
    driver.get('https://selenium-python.readthedocs.io/index.html')
    driver.maximize_window()
    logger.info('OK!')
    time.sleep(2)
    
    # Test 2
    logger.info('Klikam w interesujący mnie link')
    web = driver.find_element(by="link text", value="1. Installation")
    web.click()
    logger.info('OK!')
    time.sleep(2)
    
    # Test 3
    logger.info('Przewijam stronę na dół')
    driver.execute_script("window.scrollTo(0, 600);")
    logger.info('OK!')
    time.sleep(2)

    # Test 4
    logger.info('Przewijam stronę na górę')
    driver.execute_script("window.scrollTo(0, -400);")
    logger.info('OK!')
    time.sleep(2)

    # Test 5
    logger.info('Wracam do strony głównej')
    temp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'logo')))
    temp.click()
    logger.info('OK!')
    time.sleep(2)

except Exception as e:
    logger.error(f'Test failed: {str(e)}')

finally:
    driver.close()