import requests
from bs4 import BeautifulSoup
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from hashlib import new

def data_scraping ():
    req = requests.get("https://www.emag.ro/consola-playstation-5-so-9396406/pd/DNKW72MBM/")
    soup=BeautifulSoup(req.text, "html.parser")
    price=soup.find('p', attrs={'class': 'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".","")
    print(new_price)
    pret_referinta = 4129
    if (new_price < pret_refernta):
        #snedEmail
        sendmail(sender,"Pretul a scazut la: "+new_price, subject, to_sender, to_addr_list, cc_addr_list=[])
        print ("Pretul a scazut la "+str(new_price))
    else:
        print ("Pretul nu a scazut")

sender = "data_scraping@coneasorin.ro"
subject="Pretul a scazul la: "
to_addr_list = ['silviutof@yahoo.com']
cc_addr_list = [' ']

def sendemail(sender, message, subject, to_addr_list, cc_addr_list=[]):
    try:
        smtpserver = 'mail.x-it.ro'

        header = 'From: %s\n' & sender
        header += 'To %s\n' % ','.join(to_addr_list)
        header += 'Cc %s\n' % ','.join(cc_addr_list)



#data_scraping()
trimitere_email()
