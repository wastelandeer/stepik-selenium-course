import unittest
import time

from selenium import webdriver

def submit_form(link):
	browser = webdriver.Chrome()
	browser.get(link)

	browser.find_element_by_css_selector('.first[required]').send_keys('Some value')
	browser.find_element_by_css_selector('.second[required]').send_keys('Some value')
	browser.find_element_by_css_selector('.third[required]').send_keys('Some value')

		# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
	time.sleep(1)

		# находим элемент, содержащий текст
	welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
	return welcome_text_elt.text
	

class RegistrtaionFormSuite(unittest.TestCase):
	def test_form1(self):
		link = 'http://suninjuly.github.io/registration1.html'
		self.assertEqual(submit_form(link), "Поздравляем! Вы успешно зарегистировались!")

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		#assert  == welcome_text
	def test_form2(self):
		link = 'http://suninjuly.github.io/registration2.html'
		self.assertEqual(submit_form(link), "Поздравляем! Вы успешно зарегистировались!")

if __name__ == '__main__':
	unittest.main()