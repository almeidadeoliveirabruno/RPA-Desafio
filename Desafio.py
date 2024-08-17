import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By



#Leitura planilha
planilha = pd.read_excel('challenge.xlsx')
first_name = planilha['First Name'].values
last_name = planilha.iloc[:,1].values #Passar o nome da coluna neste caso estava dando key error.
company_name = planilha['Company Name'].values
role_in_company = planilha['Role in Company'].values
adress = planilha['Address'].values
email = planilha['Email'].values
phone = planilha['Phone Number'].values
phone = phone.astype(object)



#Automação
driver = webdriver.Chrome()
driver.get("https://rpachallenge.com/")
start = driver.find_element(By.XPATH,'/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
start.click()
for i in range(10):
    campo_nome = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelFirstName"]')
    campo_nome.send_keys(planilha['First Name'].values[i])

    campo_sobrenome = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelLastName"]')
    campo_sobrenome.send_keys(last_name[i])

    campo_empresa = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelCompanyName"]')
    campo_empresa.send_keys(company_name[i])

    campo_profissao = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelRole"]')
    campo_profissao.send_keys(role_in_company[i])

    campo_endereco = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelAddress"]')
    campo_endereco.send_keys(adress[i])

    campo_email = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelEmail"]')
    campo_email.send_keys(email[i])

    campo_telefone = driver.find_element(By.XPATH,'//input[@ng-reflect-name="labelPhone"]')
    campo_telefone.send_keys(phone[i])

    botao = driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
    botao.click()
input("Pressione Enter para fechar o navegador...")