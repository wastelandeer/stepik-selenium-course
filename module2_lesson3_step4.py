from selenium import webdriver
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('button.btn').click()
browser.switch_to.alert.accept()

x = browser.find_element_by_css_selector('#input_value').text
browser.find_element_by_css_selector('#answer[required]').send_keys(calc(x))
browser.find_element_by_css_selector('button.btn').click()

print(browser.switch_to.alert.text)
browser.quit()
