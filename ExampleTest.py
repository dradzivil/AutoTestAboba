from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://aboba.studio/ControlPanel/Reservation"
link2 = "https://aboba.studio/Account/Login"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

wait = WebDriverWait(browser, 10)

login = browser.find_element(By.ID, 'Email')
login.send_keys('darradzivil@gmail.com')
password = browser.find_element(By.ID, 'Password')
password.send_keys('627yns990G')
signin = browser.find_element(By.XPATH, '//input[@value="Войти"]')
signin.click()

create_reserve = browser.find_element(By.CLASS_NAME, 'header-booking__reservation-btn')
create_reserve.click()

date = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#date-picker')))
date.send_keys('21-06-2023')

select_table = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'option[value="45"]')))
select_table.click()

name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'create-persone__input')))
name.send_keys('Глаша')

no_phone = wait.until(EC.element_to_be_clickable((By.ID, 'no-phone-btn')))
no_phone.click()

save_button = wait.until(EC.element_to_be_clickable((By.ID, 'create-save')))
save_button.click()

browser.quit()
