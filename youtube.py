import pyautogui
import time
import keyboard
import webbrowser


pozitie_initiala_x = 512
pozitie_initiala_y = 390
pos_fin_x = 1656
pos_fin_y = 780
dif_x = 889 - pozitie_initiala_x
dif_y = pos_fin_y - pozitie_initiala_y
curent_x = 512
curent_y = 390

def autoview(curent_x,pos_fin_x,pozitie_initiala_x,pozitie_initiala_y,dif_x,curent_y,dif_y,pos_fin_y):
    time.sleep(1)
    while not keyboard.is_pressed('esc'):
        time.sleep(1)
        if curent_x<=pos_fin_x :
            pyautogui.click(curent_x,curent_y)
            print(1,curent_x,curent_y)
            curent_x=curent_x+dif_x
            time.sleep(3)
            if pyautogui.locateOnScreen(r'D:\homework\yt.png' , confidence=0.7)!= None:
                #camp_google=pyautogui.locateOnScreen(r'D:\homework\yt.png' , confidence=0.7)
                pyautogui.click(pyautogui.locateOnScreen(r'D:\homework\yt.png' , confidence=0.7))
        else:
            curent_x=pozitie_initiala_x
            time.sleep(1)
            pyautogui.move(curent_x,curent_y)
            pyautogui.scroll(-83)
            time.sleep(4)   
webbrowser.open("https://www.youtube.com/")
time.sleep(5)           
autoview(curent_x,pos_fin_x,pozitie_initiala_x,pozitie_initiala_y,dif_x,curent_y,dif_y,pos_fin_y)

def cautare_google():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'D:\homework\yt.png', confidence=0.7) !=None:
        camp_google = pyautogui.locateOnScreen(r'D:\homework\yt.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('https://www.youtube.com/watch?v=6uZIhhWsEB0')
        pyautogui.press('enter')
        pyautogui.hotkey('CTRL', 'w')

    else:
        print("Imaginea nu se afla pe ecran")


#def apasa_sub():
#    time.sleep(5)
#    if pyautogui.locateOnScreen(r'C:\Users\MAKEOUTHILL999\Pictures\heccytb\sub.png', confidence=0.7) !=None:
#            subscribe = pyautogui.locateOnScreen(r'C:\Users\MAKEOUTHILL999\Pictures\heccytb\sub.png', confidence=0.7)
#            pyautogui.click(subscribe)
#            time.sleep(1)
#            pyautogui.press('enter')

#    else:
#        print("Ai dat deja subscribe")'''

def coordonate():
    print(pyautogui.position())

col = 1
#cautare_google()
time.sleep(1)
diferenta_y = 0
while not keyboard.is_pressed('esc'):
    if col == 1:
        coordonate()
        pyautogui.onScreen(pozitie_initiala_x, pozitie_initiala_y)
        pyautogui.click()
        col = 2
    elif col == 2:
        coordonate()
        pyautogui.onScreen(pozitie_initiala_x, pozitie_initiala_y+diferenta_y)
        pyautogui.click()
        col = 3

#def click_video():
    #pyautogui

cautare_google()
apasa_sub()