from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://mail.ru/')

elem = driver.find_element_by_name('login')
elem.send_keys('study.ai_172@mail.ru')
elem.send_keys(Keys.ENTER)

time.sleep(3)
elem2 = driver.find_element_by_name('password')
elem2.send_keys('NextPassword172!')
elem2.send_keys(Keys.ENTER)

email_links = set()

for i in range(10):
    time.sleep(5)
    emails = driver.find_elements_by_xpath("//a[@class = 'llc js-tooltip-direction_letter-bottom js-letter-list-item llc_normal']")
    for email in emails:
        email_links.add(email.get_attribute('href'))
    actions = ActionChains(driver)
    actions.move_to_element(emails[-1])
    actions.perform()


result = []
for email in email_links:
    time.sleep(5)
    driver.get(email)
    time.sleep(5)
    author = driver.find_element_by_xpath("//div[@class = 'letter__author']/span[@class = 'letter-contact']").text
    date = driver.find_element_by_xpath("//div[@class = 'letter__author']/div[@class = 'letter__date']").text
    subject = driver.find_element_by_xpath("//h2[@class = 'thread__subject']").text
    email_cont = [author, date, subject]
    result.append(email_cont)
    driver.back()

pprint(result)



