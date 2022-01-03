from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

import unittest

class Test_Unittest(unittest.TestCase):
    def test_www1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код который заполняет обязательные поля
        name = browser.find_element(By.CSS_SELECTOR, "form > .first_block :nth-child(1) > input")
        name.send_keys("name")
        surname = browser.find_element(By.CSS_SELECTOR, "form > .first_block :nth-child(2) > input")
        surname.send_keys("surname")
        email = browser.find_element(By.CSS_SELECTOR, "form > .first_block :nth-child(3) > input")
        email.send_keys("email")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что могли зарегистрироваться
        # Ждем загрузку страницы
        time.sleep(1)

        # Находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # Записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be a failure")

    def test_www2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код который заполняет обязательные поля
        name = browser.find_element(By.CSS_SELECTOR, "form > .first_block :nth-child(1) > input")
        name.send_keys("name")
        surname = browser.find_element(By.CSS_SELECTOR, "form > .first_block :nth-child(2) > input")
        surname.send_keys("surname")
        email = browser.find_element(By.CSS_SELECTOR, "form > .first_block :nth-child(3) > input")
        email.send_keys("email")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что могли зарегистрироваться
        # Ждем загрузку страницы
        time.sleep(1)

        # Находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # Записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be a failure")
if __name__ == "__main__":
    unittest.main()

