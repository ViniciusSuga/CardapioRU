from selenium import webdriver
from selenium.webdriver.common.by import By

class Cardapio:

    def __init__(self,driver):
        self.driver = driver
        self.url = "http://www.ru.uem.br/cardapio-1"
        self.pratosegunda = '/html/body/div[1]/div[2]/div[1]/div[2]/div[5]/div/div[4]/table/tbody/tr[1]/td/p[3]'  #Xpath
        self.pratoterca = '/html/body/div[1]/div[2]/div[1]/div[2]/div[5]/div/div[7]/table/tbody/tr[1]/td/p[3]'  #Xpath
        self.pratoquarta = '/html/body/div[1]/div[2]/div[1]/div[2]/div[5]/div/div[9]/table/tbody/tr[1]/td/p[3]'  #Xpath
        self.pratoquinta = '/html/body/div[1]/div[2]/div[1]/div[2]/div[5]/div/div[12]/table/tbody/tr[1]/td/p[3]'  #Xpath
        self.pratosexta = '/html/body/div[1]/div[2]/div[1]/div[2]/div[5]/div/div[13]/table/tbody/tr[1]/td/p[3]'  #Xpath

    def navigate (self):
        self.driver.get(self.url)


    def getPrato(self):
        semana = []
        pratos = [self.pratosegunda,self.pratoterca,self.pratoquarta,self.pratoquinta,self.pratosexta]
        for i in pratos:
            pratodia = self.driver.find_element(By.XPATH,i).text
            semana.append(pratodia)
        return semana


driver = webdriver.Firefox()
c = Cardapio(driver)


c.navigate()
c.getPrato()