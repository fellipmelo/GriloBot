'''


#-----------------------
#
#   GriloBot by Fellip Melo
#
#   segue la meu rei: https://instagram.com/fellipmg
#   
#   Linkedin    https://linkedin.com/in/fellipmelo
#   
#   Youtube     https://www.youtube.com/channel/UC1cRedG4bvPdfPLpYNRYxJg   
#------------------------
# -*- coding: utf-8 -*-



'''

from selenium import webdriver
from time import sleep
import random
import os
import random






###########################################################################
# cores
DD = ''
CC = ''
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'

###########################################################################
# banner

os.system('cls')

def banner():
    
    
    print(verde + """

                          ____          _   _           ____        _   
                         / ___|  _ __  (_) | |   ___   | __ )  ___ | |_ 
                        | |  _  | '__| | | | |  / _ \  |  _ \ / _ \| __|
                        | |_| | | |    | | | | | (_) | | |_) | (_) | |_ 
                         \____| |_|    |_| |_|  \___/  |____/ \___/ \__|
                                                            


                                By FELLIP MELO 

                   https://instagram.com/fellipMG
                       https://github.com/fellipmelo
                            https://linkedin.com/in/fellipmelo

                                                
    """)
    sleep(3)



    #############################################################
    #  Tags

tags = ["https://www.instagram.com/explore/tags/passinho/",
        "https://www.instagram.com/explore/tags/maloka", 
        "https://www.instagram.com/explore/tags/passinhodosmaloka", 
        "https://www.instagram.com/explore/tags/instagram/",
        "https://www.instagram.com/explore/tags/kalilinux/",
        "https://www.instagram.com/explore/tags/uberlandia/", 
        "https://www.instagram.com/explore/tags/tiktokbrasil/",
        "https://www.instagram.com/explore/tags/ethicalhacker/",
        "https://www.instagram.com/explore/tags/tiktok",
        "https://www.instagram.com/explore/tags/ccbfashion",
        "https://www.instagram.com/explore/tags/igreja/",
        "https://www.instagram.com/explore/tags/fsociety/",
        "https://www.instagram.com/explore/tags/ccbbrasil/",
        "https://www.instagram.com/explore/tags/jesus/",
        "https://www.instagram.com/explore/tags/python/",
        "https://www.instagram.com/explore/tags/cristã/",
        "https://www.instagram.com/explore/tags/ieq/",]


##############################################################
#  definições gerais
optionss = webdriver.ChromeOptions()
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")
browser = webdriver.Chrome(executable_path=r"bot/chromedriver.exe", options=optionss)





###############################################################
#  abre navegador

def start():

    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(10)
    # login
    username = browser.find_element_by_name('username')
    username.send_keys(DD)
    password = browser.find_element_by_name('password')
    password.send_keys(CC)
    try:
        enter = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
        enter.click()
    except Exception:
        enter = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
        enter.click()
    sleep(10)
    # notificação cancelar
    notificacao = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
    notificacao.click()
    sleep(3)
############################################################################
#  curti fotos por hastag

def curti_por_hastag():
    browser.get(random.choice(tags))
    sleep(10)
    primeiro_post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div')
    primeiro_post.click()
    sleep(10)
    curtir = browser.find_element_by_class_name('wpO6b ')
    curtir.click()
    sleep(10)
    proximo_post = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
    proximo_post.click()
    sleep(10)

    # curtir repetição
    numero_de_fotos_para_curtir = int(4)
    numero_ficticio = int(1)
    while numero_ficticio < numero_de_fotos_para_curtir:
        sleep(10)
        numero_ficticio = numero_ficticio + int(1)
        curtir = browser.find_element_by_class_name('wpO6b ')
        curtir.click()
        sleep(10)
        proximo_post = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        proximo_post.click()

#########################################################################
# Seguir por hastag

def seguir_por_hastag():
    browser.get(random.choice(tags))
    sleep(10)
    primeiro_post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div')
    primeiro_post.click()
    sleep(10)
    # seguir repetição
    numero_de_perfis_para_seguir = int(20)
    numero_ficticio = int(0)
    while True:
        if numero_ficticio == numero_de_perfis_para_seguir:
            break
        else:
            numero_ficticio = numero_ficticio + int(1)
            try: 
                # pegar nome de usuário e salvar
                user_nome = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
                with open('usuarios_seguidos.txt') as f:
                    for l_num, l in enumerate(f, 1): # percorrer linhas e enumera-las a partir de 1
                        if user_nome in l: # ver se palavra esta na linha
                            break
                    else: # caso não haja break
                        print('Novo usuário seguido ' + user_nome + ' \n Adicionando a Lista ... \n ')
                        usuarios_seguidos = open('usuarios_seguidos.txt', 'a')
                        usuarios_seguidos.write(user_nome + '\n')
                        usuarios_seguidos.close()
   
                # segue usuário
                seguir = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
                seguir.click()
                sleep(10)
                proximo_post = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                proximo_post.click()
                sleep(10)
            except:
                proximo_imagem = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                proximo_imagem.click()
                sleep(10)
                
##############################################################################
# curtir e seguir por hastag

def curti_e_seguir_por_hastag():
    browser.get(random.choice(tags))
    sleep(10)
    primeiro_post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div')
    primeiro_post.click()
    sleep(10)
    # seguir repetição
    numero_de_perfis_para_seguir = int(30)
    numero_ficticio = int(0)
    while True:
        if numero_ficticio == numero_de_perfis_para_seguir:
            break
        else:
            numero_ficticio = numero_ficticio + int(1)
            try: 
                user_nome = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
                with open('usuarios_seguidos.txt') as f:
                    for l_num, l in enumerate(f, 1): # percorrer linhas e enumera-las a partir de 1
                        if user_nome in l: # ver se palavra esta na linha
                            break
                    else: # caso não haja break
                        print('Novo usuário seguido [' + user_nome + '] \n Adicionando a Lista ... \n ')
                        usuarios_seguidos = open('usuarios_seguidos.txt', 'a')
                        usuarios_seguidos.write(user_nome + '\n')
                        usuarios_seguidos.close()
                # segue e curti
                seguir = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
                seguir.click()
                sleep(17)
                try:
                    curtir = browser.find_element_by_class_name('wpO6b ')
                    curtir.click()
                    sleep(17)
                except Exception:
                    sleep(10)
                    cancelar = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[2]')
                    cancelar.click()
                proximo_post = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                proximo_post.click()
                sleep(17)
            except:
                proximo_imagem = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                proximo_imagem.click()
                sleep(17)
                


#####################################################################
#  curti por localização

def curtir_por_localizacao():
    localizacao = browser.get('https://www.instagram.com/explore/locations/213876111/uberlandia/')
    localizacao
    sleep(10)
    primeiro_post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div')
    primeiro_post.click()
    sleep(10)
    curtir = browser.find_element_by_class_name('wpO6b ')
    curtir.click()
    sleep(10)
    proximo_post = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
    proximo_post.click()
    sleep(10)

    # curtir repetição
    numero_de_fotos_para_curtir = int(4)
    numero_ficticio = int(1)
    while numero_ficticio < numero_de_fotos_para_curtir:
        sleep(10)
        numero_ficticio = numero_ficticio + int(1)
        curtir = browser.find_element_by_class_name('wpO6b ')
        curtir.click()
        sleep(10)
        proximo_post = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
        proximo_post.click()
    
#####################################################################
# seguir por localização

def seguir_por_localizacao():
    localizacao = browser.get('https://www.instagram.com/explore/locations/213876111/uberlandia/')
    localizacao
    sleep(10)
    primeiro_post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div')
    primeiro_post.click()
    sleep(10)
    # seguir repetição
    numero_de_perfis_para_seguir = int(4)
    numero_ficticio = int(0)
    while True:
        if numero_ficticio == numero_de_perfis_para_seguir:
            break
        else:
            numero_ficticio = numero_ficticio + int(1)
            try: 
                user_nome = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
                with open('usuarios_seguidos.txt') as f:
                    for l_num, l in enumerate(f, 1): # percorrer linhas e enumera-las a partir de 1
                        if user_nome in l: # ver se palavra esta na linha
                            break
                    else: # caso não haja break
                        print('Novo usuário seguido [' + user_nome + '] \n Adicionando a Lista ... \n ')
                        usuarios_seguidos = open('usuarios_seguidos.txt', 'a')
                        usuarios_seguidos.write(user_nome + '\n')
                        usuarios_seguidos.close()
                # começa a seguir por localização
                seguir = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
                seguir.click()
                sleep(10)
                proximo_post = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                proximo_post.click()
                sleep(10)
            except:
                proximo_imagem = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                proximo_imagem.click()
                sleep(10)


#################################################################################
# curtir e seguir por localização

def curti_e_seguir_por_localizacao():
    localizacao = browser.get('https://www.instagram.com/explore/locations/213876111/uberlandia/')
    localizacao
    sleep(10)
    primeiro_post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div')
    primeiro_post.click()
    sleep(10)
    # seguir repetição
    numero_de_perfis_para_seguir = int(4)
    numero_ficticio = int(0)
    while True:
        if numero_ficticio == numero_de_perfis_para_seguir:
            break
        else:
            numero_ficticio = numero_ficticio + int(1)
            try: 
                user_nome = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
                with open('usuarios_seguidos.txt') as f:
                    for l_num, l in enumerate(f, 1): # percorrer linhas e enumera-las a partir de 1
                        if user_nome in l: # ver se palavra esta na linha
                            break
                    else: # caso não haja break
                        print('Novo usuário seguido [' + user_nome + '] \n Adicionando a Lista ... \n ')
                        usuarios_seguidos = open('usuarios_seguidos.txt', 'a')
                        usuarios_seguidos.write(user_nome + '\n')
                        usuarios_seguidos.close()

                # segue e curti por localização
                seguir = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
                seguir.click()
                sleep(10)
                curtir = browser.find_element_by_class_name('wpO6b ')
                curtir.click()
                sleep(10)
                proximo_post = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                proximo_post.click()
                sleep(10)
            except:
                proximo_imagem = browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]')
                proximo_imagem.click()
                sleep(10)


##################################################################
# deseguir usuários 
def deixar_de_seguir_usuarios_seguidos():
    base_usuarios = open('usuarios_seguidos.txt', 'r')
    AA = 600
    BB = 1

    while AA > BB:
        try:
            BB = BB + 1
            usuario = base_usuarios.readline()
            browser.get("https://www.instagram.com/" + usuario)
            sleep(12)

            verificar_seguir = browser.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button').text
            verificar_seguir_de_volta = browser.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button').text
            base_usuarios_erro = open('base_usuarios_erro.txt', 'a')
            nome_usuario = browser.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > h2').text
            if verificar_seguir == 'Seguir':
                print('Usuário já era deseguido -->  ' + nome_usuario)
                base_usuarios_erro.write('\nUsuário já era deseguido -->> ' + nome_usuario)
                base_usuarios_erro.close()
                    
            elif verificar_seguir_de_volta == 'Seguir de volta':
                print('Usuário já era deseguido -->  ' + nome_usuario)
                base_usuarios_erro.write('\nUsuário já era deseguido -->> ' + nome_usuario)        
                base_usuarios_erro.close()
            else:    
                try:
                    botao_seguindo = browser.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button')
                    botao_seguindo.click()
                    sleep(15)
                    botao_deixar_de_seguir = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
                    botao_deixar_de_seguir.click()
                    base_usuarios_erro.write('\nUsuário deseguido -->> ' + nome_usuario)
                    base_usuarios_erro.close()
                    print('\nUsuário deseguido -->> ' + nome_usuario)
                    sleep(15)
                    
                except Exception:
                    sleep(3)
                    print('Já estava seguindo o usuário -->> ' + nome_usuario)
                    botao_seguindo = browser.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button')
                    botao_seguindo.click()
                    sleep(15)
                    botao_deixar_de_seguir = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]')
                    botao_deixar_de_seguir.click()
                    sleep(15)
          
        except:
             
            print('Deu erro ')
            sleep(30)  

start()
while True:
    curti_e_seguir_por_hastag()

#647

#crista




















