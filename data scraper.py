import string
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from hashlib import new
import smtplib
sender='data_scraping@coneasorin.ro'
subject='Pretul a scazut la:'
to_addr_list = ['silviutof@yahoo.com']
cc_addr_list = ['']
def sendemail(sender,message, subject,to_addr_list, cc_addr_list=[]):
    try:
        smtpserver='mail.x-it.ro:26'
        header  = 'From: %s\n' % sender
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender,"stiinte217_2022")
        problems = server.sendmail(sender, to_addr_list, message)
        server.quit()
        return True
    except:
        return False


def data_scraping ():
    req=requests.get("https://www.emag.ro/consola-playstation-5-so-9396406/pd/DNKW72MBM/")
    soup=BeautifulSoup(req.text,"html.parser")
    price=soup.find('p', attrs={'class': 'product-new-price'}).text
    new_price=price[0:5]
    new_price=new_price.replace(".","")
    new_price=int(new_price)
    pret_referinta = 7079
    if(new_price<pret_referinta):
        sendemail(sender,"Pretul a scazut" , subject,to_addr_list, cc_addr_list=[])
        print("Pretul a scazut")
    else:
        print("pretul a crescut")

sendemail(sender,"Pretul a scazut" , subject,to_addr_list, cc_addr_list=[])