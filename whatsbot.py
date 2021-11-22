from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import requests
from selenium.webdriver import Chrome , Firefox
from selenium.webdriver.common.keys import Keys
from time import sleep
from unicodedata import normalize

def remover_acentos(txt):
	return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')



browser = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://web.whatsapp.com/'
browser.get(url)
input('Read QRCode before press ENTER:')

arq = open('tel.txt','r')
list_of_numbers = arq.readlines()
arq.close()
quant = len(list_of_numbers)
arq = open('text.txt','r')
text = arq.readlines()
arq.close()

for tel in list_of_numbers:
	url = f'https://web.whatsapp.com/send?phone=55{tel}'
	browser.get(url)
	sleep(5)

	try:
		aux = browser.find_element_by_xpath('//*[@id="main"]/footer/div/div/div/div/div/div/div[@class="_13NKt copyable-text selectable-text"]')
		aux.click()
		for line in text:
			aux_line = line
			aux_line = aux_line.replace('\n','')
			aux.send_keys(aux_line)
			aux.send_keys(Keys.SHIFT + Keys.RETURN)
		aux.send_keys(Keys.RETURN)
		sleep(2)
		aux.send_keys(Keys.RETURN)
	except:
		pass
	print(f'restam o numero {quant} ')
	quant-=1