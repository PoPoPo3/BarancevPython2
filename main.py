# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time


class CashOrderKRD(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_cash_order_k_r_d(self):
        driver = self.driver
        self.driver.get("https://rocknrolls23.ru/")
        self.driver.set_window_size(1920, 1020)
        self.driver.find_element(By.LINK_TEXT, "Меню").click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div/div/div[1]/div/div[3]/div[6]/a").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div/div/div[2]/div/div[3]/div[6]/a").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[5]/div/div/div[4]/div/div[3]/div[6]/a").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/header/div[3]/div[2]/div[2]/div[2]/p[1]/a").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, "Перейти в КОРЗИНУ").click()
        self.driver.implicitly_wait(2)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[4]/button").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, "order_name").click()
        self.driver.find_element(By.ID, "order_name").send_keys("Тест")
        self.driver.find_element(By.ID, "order_phone").click()
        self.driver.find_element(By.ID, "order_phone").send_keys("+79182529384")
        self.driver.find_element(By.ID, "order_street").click()
        self.driver.find_element(By.ID, "order_street").send_keys("Думенко")
        self.driver.find_element(By.ID, "order_house").click()
        self.driver.find_element(By.ID, "order_house").send_keys("12")
        self.driver.find_element(By.ID, "order_comment").click()
        self.driver.find_element(By.ID, "order_comment").send_keys("ТЕСТ НЕ ГОТОВИТЬ")
        self.driver.find_element(By.ID, "order_intercome").click()
        self.driver.find_element(By.ID, "order_intercome").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) i").click()
        time.sleep(2)
        # self.driver.find_element(By.ID, "sendOrder").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()