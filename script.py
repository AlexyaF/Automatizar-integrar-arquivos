from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import os
from time import sleep

servico = Service(ChromeDriverManager().install()) # Identifica a versão do navegador atual e vai baixar o Chrome Driver mais recente.

navegador = webdriver.Chrome()

navegador.get("https://site.exemplo/")


#Buscar o elemento e escrever o usuário
navegador.find_element('xpath', '//*[@id="formulario"]/div[1]/input').send_keys('EX')
navegador.find_element('xpath', '//*[@id="formulario"]/div[2]/input').send_keys('EX')

#Entrar
navegador.find_element('xpath', '//*[@id="btentrar"]').click()

#Buscar tela de integracao
try:
    navegador.find_element('xpath', '//*[@id="field5"]').send_keys("Retorno Exemplo")
    sleep(5)

    # Aguarda o elemento ficar visível
    wait = WebDriverWait(navegador, 10)  # Substitua 'navegador' pelo nome do driver
    element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="field5-suggestions"]//span[text()="RETORNO Exemplo"]')))
    element.click()
except:
    print("ERRO!")


#arquivos
pathFolder = r"\\Exemplo\Caminho"
files = os.listdir(pathFolder)
allpath = os.path.join(pathFolder, files[0])
allpath


wait = WebDriverWait(navegador, 10) # Aguarda até o elemento estar visível
navegador.switch_to.frame("cont") # mudando para o iframe
input_element = wait.until(EC.visibility_of_element_located((By.ID, 'Upload1'))) #aguardo até a visibilidade do elemento e identifico 
input_element.send_keys(allpath) #envio o arquivo 