from tkinter import RIGHT
import pyautogui as pt 
import pyperclip as pc 
from pynput.mouse import Controller , Button 
from time import sleep
from whatsapprespo import response
import os
os.chdir('C:/Users/saksh/OneDrive/Desktop/Java')

mouse = Controller ()

class WhatsApp: 
    def __init__(self,speed=100.0,click_speed =100.0 ):
        self.speed = speed 
        click_speed = click_speed 
        self_message = ''
        last_message = ''

#from pyautogui import position


def new_msg(self):
    try: 
        position = pt.locateOnScreen('green dot.png', confidence = .8)
        pt.moveTo(position[0:2],duration=self.speed)
        pt.moveRel(-100,0,duration=self.speed)
        pt.doubleClick(interval=self.speed)
    except  Exception as e :
        print('Exception (green_dot): ' , e)
def text_box(self):
    try :
        position = pt.locateOnScreen('smile.png', confidence = .9)
        pt.moveTo(position[0:2],duration=self.speed)
        pt.moveRel(200,20,duration=self.speed)
        pt.doubleClick(interval=self.speed)
    except  Exception as e :
        print('Exception (smile): ' , e)



def nav_mess(self):
    try :
        position = pt.locateOnScreen('smile.png', confidence = .9)
        pt.moveTo(position[0:2],duration=self.speed)
        pt.moveRel(120,-65,duration=self.speed)
        pt.tripleClick(interval=self.speed)
    except  Exception as e :
        print('Exception (smile): ' , e)


def get_msg(self):
    mouse.click(Button.left,3)
    sleep(self.speed)
    mouse.click(Button.right,1)
    sleep(self.speed)
    pt.moveRel(30,-200 ,duration=self.speed)
    mouse.click(Button.left,1)

    self.message = pc.paste()
    print('User says:', self.message)

def send_msg(self):
    try:
            bot_respo=response(self.message)
            print('You say:',bot_respo)
            pt.typewrite(bot_respo,interval=.1)
            pt.typewrite('\n')

            #self.last_message =self.message
        
    except Exception as e:
        print('Exception (send_msg):',e)
   #dout
    for new_msg in send_msg :
         print(send_msg)


wa_bot = WhatsApp(speed = .8, click_speed=.7)
sleep(2)

new_msg(wa_bot)
nav_mess(wa_bot)
get_msg(wa_bot)
text_box(wa_bot)
send_msg(wa_bot)