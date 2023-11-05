from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tabulate import tabulate
from selenium.common.exceptions import NoSuchElementException
import time
import os
#converti prezzo che trovi sul sito in una stringa che posso trasformare usando la funzione int()
def format(str):
    if ',' in str:
        str=str.replace(',','')
    if ' KR' in str:
        str=str.replace(' KR','')
    return str    
normal_XPATH='/html/body/div[2]/div[15]/div[2]/div[2]/div[2]'
animated_XPATH='/html/body/div[2]/div[15]/div[2]/div[2]/div[3]'
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/demor/.config/chromium/Profile 2/')
driver = webdriver.Chrome(options=options)
headers = ["index","best price","margine","ratio"]
link='https://krunker.io/social.html?p=market&i='
all_rows=[]
#DA CAMBIARE IN BASE ALLE PROPRIE PREFERENZE
#il margine minimo conta anche le tasse della vendita
min_margine=200
#index minimo e massimo da guardare
START=100
END=8000
#SE VOGLIO FILTRARE LE SKIN CON AL MASSIMO IL MIO SALDO FACCIO COSÌ,ALTRIMENTI LO DICHIARO A MANO
#mykr=driver.find_element(By.ID,'profileKR').text
#mykr=format(mykr)
#mykr=int(mykr)
mykr=3000
#tempo da aspettare prima di cambiare pagina dicendo che non trova l'elemento
driver.implicitly_wait(2)
for i in range(START,END):
    print("index : "+str(i))
    row=[]
    driver.get(link+str(i))
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
        second=driver.find_element(By.XPATH,normal_XPATH).text
        if (second == ''):
            #se non faccio cosí con gli sticker animati si rompe tutto
            #devo ancora trovare XPATH giusto,ma cosí almeno non si blocca
            second=driver.find_element(By.XPATH,animated_XPATH).text
        second=format(second)
        second_price=int(second)
    except NoSuchElementException:
        second_price=0 
    #print(str(best_price)+" "+str(second_price))
    if mykr>best_price and second_price>min_margine:
        delta=second_price-best_price
        #guadagno massimo - tassa massima sul prezzo inferiore al secondo
        margine=delta-round((second_price-1)/10)
        if margine>min_margine and best_price<mykr:
            row.append(i)
            row.append(best_price)
            #row.append(delta)
            row.append(margine)
            ratio=margine/best_price
            row.append(ratio)
            print(all_rows)
            #non usare append ma fare insert ed usare index in base a come rapporto margine/costo
            #controllare ogni riga partendo dalla prima se ratio é maggiore,se é cosí insert a quell'index altrimenti aumenta index e fai check
            leng=len(all_rows)-1
            #se non si mette uguale sbaglia quando c'é solo un elemento e mette sempre in fondo il secondo anche se il ratio é maggiore
            if (leng>=0):
                k=0
                while k<=leng:
                    print(str(ratio)," ",str(all_rows[k][3]))
                    if(ratio>=all_rows[k][3]):
                        all_rows.insert(k,row)
                        break
                    else:
                        k+=1
                if k==leng+1:
                    all_rows.append(row)
            else:
                all_rows.append(row)
            os.system("clear")
            print(tabulate(all_rows, headers, tablefmt="simple_grid"))
    else:
        pass
