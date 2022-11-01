from selenium import webdriver
from selenium.webdriver.common.by import By

class Cardapio:

    def __init__(self,driver):
        self.driver = driver
        self.url = "http://www.ru.uem.br/cardapio-1"
        self.lista = ['4','7','9','12','13']
        self.inicio = '/html/body/div[1]/div[2]/div[1]/div[2]/div[5]/div/div['
        self.fim = ']/table/tbody/tr[1]/td/p[3]'


    def navigate (self):
        self.driver.get(self.url)


    def getPrato(self):
        semana = []
        pratos = []
        for i in self.lista:
            xpath = self.inicio + i + self.fim
            pratos.append(xpath)
        for i in pratos:
            pratodia = self.driver.find_element(By.XPATH,i).text
            semana.append(pratodia)
        return semana