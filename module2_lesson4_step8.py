from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '10000'))
browser.find_element_by_css_selector('button#book').click()

x = browser.find_element_by_css_selector('#input_value').text
browser.find_element_by_css_selector('#answer[required]').send_keys(calc(x))
browser.find_element_by_css_selector('button#solve').click()

print(browser.switch_to.alert.text)
browser.quit()