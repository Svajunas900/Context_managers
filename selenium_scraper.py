from selenium import webdriver
from selenium.webdriver.common.by import By


def write_text_from_wiki(user_text, file_name):
  driver = webdriver.Chrome()
  driver.get("https://www.wikipedia.org/")
  search_input = driver.find_element(by=By.XPATH, value='//*[@id="searchInput"]')
  search_input.send_keys(user_text)
  search_button = driver.find_element(by=By.XPATH, value='//*[@id="search-form"]/fieldset/button')
  search_button.click()
  text = driver.find_element(by=By.XPATH, value='//*[@id="mw-content-text"]/div[1]')
  write_text_to_file(text.text, file_name)
  driver.quit()


def write_text_to_file(text, file_name):
  with open(file_name, 'w', encoding="utf8") as file:
    file.write(text)