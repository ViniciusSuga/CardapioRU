import crawler
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
c = crawler.Cardapio(driver)
c.navigate()
pratos = c.getPrato()

