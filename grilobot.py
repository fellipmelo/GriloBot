#-----------------------
#
#   Instabot by Fellip Melo
#
#   segue la meu rei: https://instagram.com/fellipsec
#------------------------
# -*- coding: utf-8 -*-


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string
import os
import getpass 
import sys
import argparse

# cores 

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'


#banner

os.system('cls')

def banner():

    print(verde + """


                            _           _   _           _        
                            | |__   ___ | |_(_)_ __  ___| |_ __ _ 
                            | '_ \ / _ \| __| | '_ \/ __| __/ _` |
                            | |_) | (_) | |_| | | | \__ \ || (_| |
                            |_.__/ \___/ \__|_|_| |_|___/\__\__,_|



                                                By Fellip Melo


                   https://instagram.com/fellipMG
                       https://github.com/fellipmelo
                            https://linkedin.com/in/fellipmelo

                                                
    """)
    sleep(8)
    

#  tags  

tags = ["https://www.instagram.com/explore/tags/fellipsec/",
        "https://www.instagram.com/explore/tags/kalilinux", 
        "https://www.instagram.com/explore/tags/infosec", 
        "https://www.instagram.com/explore/tags/cybersecurity/",
        "https://www.instagram.com/explore/tags/pentest/",
        "https://www.instagram.com/explore/tags/ti/", 
        "https://www.instagram.com/explore/tags/tidadepressao/",
        "https://www.instagram.com/explore/tags/ethicalhacker/",
        "https://www.instagram.com/explore/tags/hacker/",
        "https://www.instagram.com/explore/tags/programming/",
        "https://www.instagram.com/explore/tags/hacktheworld/",
        "https://www.instagram.com/explore/tags/fsociety/",
        "https://www.instagram.com/explore/tags/ccna/",
        "https://www.instagram.com/explore/tags/programmerhumor/",
        "https://www.instagram.com/explore/tags/python/",
        "https://www.instagram.com/explore/tags/oscp/",
        "https://www.instagram.com/explore/tags/developers/",]

# inicia bot

def start():
   
    browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    sleep(10)
    user_name = browser.find_element_by_name("username")
    user_name.send_keys(agrs.u)
    senha = browser.find_element_by_name("password")
    senha.send_keys(agrs.p)
    entrar = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
    entrar.click()

    # notificacao " agora nao"

    sleep(5)
    notificacao = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
    sleep(3)
    notificacao.click()
    sleep(3)
    # abre um link e clica em uma foto para iniciar programa

    browser.get(random.choice(tags))
    sleep(8)
    post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]')
    browser.implicitly_wait(1) 
    post.click()


def repeticao():
    
    browser.get(random.choice(tags))
    sleep(6)
    post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]')
    browser.implicitly_wait(1) 
    post.click()
    if a == '1':
        likes()
    else:
        curtir_seguir()


 
# comecar a curtir as fotos

def likes():
    for repete in range(50):

        sleep(5)

        curtir = browser.find_element_by_class_name('wpO6b ') 
        curtir.click()

        sleep(5)

        proximo_imagem = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        proximo_imagem.click()
      

#  curtir e seguir


def curtir_seguir():
    for repete in range(50):
        sleep(4)

        curtir = browser.find_element_by_class_name('wpO6b ') 
        curtir.click()
        sleep(5)
        def seguir_user():
            seguir = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
            seguir.click()
            sleep(7)
        try:
            seguir_user()
        except Exception:
            sleep(2)


        # deixar de segui caso ja esteja seguindo
        try:
            proximo_imagem = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
            proximo_imagem.click()
            
        except Exception:
            deseguir = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]')
            deseguir.click()
            sleep(4)
            proximo_imagem = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
            proximo_imagem.click()

def deseguir():
    browser.get("https://instagram.com/" + agrs.u)
    sleep(4)
    clicar_seguindo = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
    clicar_seguindo.click()
    sleep(4)

    def deseguir_user():
        des1 = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button')
        des1.click()
        sleep(1)
        #localiza bt confirmar deixar de seguir
        des_confir = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]')

        des_confir.click()
        # inicia deseguimento
        sleep(4)
        des2 = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[2]/div/div[3]/button')
        des2.click()
        sleep(2)
        des_confir = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]')
        des_confir.click()
        # inicia
        sleep(4)
        des3 = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[3]/div/div[3]/button')
        des3.click()
        sleep(2)
        des_confir = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]')
        des_confir.click()  # finaliza
        sleep(4)
        des4 = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[4]/div/div[3]/button')
        des4.click()
        sleep(2)
        des_confir = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]')
        des_confir.click()
        sleep(5)
        des5 = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[5]/div/div[3]/button')
        des5.click()
        sleep(2)
        des_confir = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]')
        des_confir.click()
        sleep(4)
        des6 = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[6]/div/div[3]/button')
        des6.click()
        des_confir = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]')
        des_confir.click()
        

        sleep(3)
        fechar = browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')
        fechar.click()
        sleep(15)
    
    # chama funcao deseguir
    deseguir_user()

        

 

# recebe os argumentos da linha de comando

parser = argparse.ArgumentParser(description = 'Loguin')
parser.add_argument('-u', required= True)
parser.add_argument('-p', required= True)

agrs = parser.parse_args()

banner()

print(vermelho + """

 Selecione uma das opções abaixo:


 1) Curtir
 2) Curtir e seguir
 3) Deixar de seguir

""")

a = '1'

selecione = str(input(verde +"#$ "))
if selecione == '1':
    #a = '1'
    browser = webdriver.Chrome(executable_path=r"bot/chromedriver.exe")
    start()
    likes()
    for curtir in range(2000):
        repeticao()

elif selecione == '2':
    #a = '2'
    browser = webdriver.Chrome(executable_path=r"bot/chromedriver.exe")
    start()
    curtir_seguir()
    for curtir_seguir in range(5000):
        repeticao()
elif selecione == '3':
    #a = '3'
    print('')
    valor = int(input(" Quantas pessoas quer deseguir ? "))
    b = 7
    valor = valor / 7
    valor = round(valor)
    browser = webdriver.Chrome(executable_path=r"bot/chromedriver.exe")
    start()
    deseguir()
    for unfollow in range(valor):
        deseguir()


#start()
#curtir_seguir()
#for curtir_seguir in range(5):
 #   repeticao()