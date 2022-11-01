import crawler_selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
c = crawler_selenium.Cardapio(driver)
c.navigate()
pratos = c.getPrato()
print (pratos)