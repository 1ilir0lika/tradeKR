from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tabulate import tabulate
from selenium.common.exceptions import NoSuchElementException
import time
import os
def format(str):
    if ',' in str:
        str=str.replace(',','')
    if ' KR' in str:
        str=str.replace(' KR','')
    return str    
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/demor/.config/chromium/Profile 2/')
driver = webdriver.Chrome(options=options)
headers = ["index","best price","delta","margine"]
link='https://krunker.io/social.html?p=market&i='
all_rows=[]
min_margine=100
#SE VOGLIO FILTRARE LE SKIN CON AL MASSIMO IL MIO SALDO FACCIO COSÌ,ALTRIMENTI LO DICHIARO A MANO
#mykr=driver.find_element(By.ID,'profileKR').text
#mykr=format(mykr)
#mykr=int(mykr)
mykr=2500
#tempo da aspettare prima di cambiare pagina dicendo che nontrova l'elemento
driver.implicitly_wait(2)
for i in range(0,8000):
    print("index : "+str(i))
    row=[]
    driver.get(link+str(i))
    #time.sleep(1)
    #prices=driver.find_element(By.XPATH,'/html/body/div[2]/div[15]/div[2]/div[1]/div[2]')
    try:
        best=driver.find_element(By.CLASS_NAME,'marketCard').text
        if (best != ''):
            best=format(best)
            best_price=int(best.split('\n')[2])
        else:
            best_price=0
    except NoSuchElementException:
        best_price=0
    try:
        second=driver.find_element(By.XPATH,'/html/body/div[2]/div[15]/div[2]/div[2]/div[2]').text
        if (second == ''):
            #se non faccio cosí con gli sticker animati si rompe tutto
            second=driver.find_element(By.XPATH,'/html/body/div[2]/div[15]/div[2]/div[2]/div[3]').text
        second=format(second)
        second_price=int(second)
    except NoSuchElementException:
        second_price=0 
    #debuga=best[:-3].split('\n')[2]
    #debugb=second[:-3]
    print(str(best_price)+" "+str(second_price))
    if mykr>best_price and second_price>min_margine:
        delta=second_price-best_price
        #guadagno massimo - tassa massima sul prezzo inferiore al secondo
        margine=delta-round((second_price-1)/10)
        if margine>min_margine and best_price<mykr:
            row.append(i)
            row.append(best_price)
            row.append(delta)
            row.append(margine)
            all_rows.append(row)
            os.system("clear")
            print(tabulate(all_rows, headers, tablefmt="simple_grid"))
    else:
        pass
#time.sleep(10)
