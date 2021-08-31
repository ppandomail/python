from selenium import webdriver
import unittest
import time


class MyTestCase(unittest.TestCase):

    def test_no_results(self):
        driver = webdriver.Chrome('/Users/ppando/PycharmProjects/proy_python/Selenium/chromedriver')
        driver.get('http://automationpractice.com/index.php')
        driver.find_element_by_id('search_query_top').send_keys('Hola')
        driver.find_element_by_name('submit_search').click()
        time.sleep(10)
        actual = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        self.assertEqual('No results were found for your search "Hola"', actual)
        time.sleep(2)
        driver.find_element_by_link_text("Women").click()
        time.sleep(2)
        driver.find_element_by_partial_link_text("Dres").click()
        time.sleep(2)
        driver.close()
        driver.quit()

