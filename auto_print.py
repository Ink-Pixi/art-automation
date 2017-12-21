import os
import subprocess
import ctypes
import sys
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time
from rsa import key

__ink_type = 'w'
__highlight = 9
__mask = 2
__use_background = False
__multiple_pass = True
__transparent_color = False # cmykw and w only
__transparent_red = str(67)
__transparent_green = str(47)
__transparent_blue = str(35)
__tolorance = 50
__min_white = 2
__choke_width = 3
__wht_color_pause = True
__saturation = 30
__brightness = 40
__contrast = 20
__uni_printing = True
__ink_volumne = 6 #starts at 1 so 1 == 0, 2 == 1 etc
__dbl_printing = 1


m = PyMouse()
k = PyKeyboard()

word_doc = '/TEST.docx'
#word_path = os.path.join('C:\Program Files (x86)\Microsoft Office\Office14\WINWORD.EXE', word_doc)

open_word = subprocess.Popen(['C:\Program Files (x86)\Microsoft Office\Office14\WINWORD.EXE', word_doc])
time.sleep(2)

# k.press_keys([k.alt_r_key, k.space])
# 
# k.tap_key(k.down_key, 4, 0)
# 
# k.tap_key(k.enter_key)
# time.sleep(.5)
# screen = m.screen_size()
# print(screen)
#  
# #select test name 
# m.click(600,700, 1, 2)
# #replace with david
# for l in 'David':
#     k.tap_key(l)

#MAKE SURE BROTHER IS DEFAULT PRINTER!!!
#open the print dialog
k.press_key(k.control_r_key)
k.tap_key('p')
k.release_key(k.control_r_key)

#pause    
time.sleep(1)
#move to Printer Properties
k.tap_key(k.tab_key, 3)
#open Printer Properties    
k.tap_key(k.enter_key)
#pause
time.sleep(1)

#move to select ink
k.tap_key(k.tab_key, 3)
if __ink_type == 'cmykw':
    #move to Highlight slider
    k.tap_key(k.tab_key, 2)
elif __ink_type == 'w':
    k.tap_key(k.down_key)
    #move to Highlight slider
    k.tap_key(k.tab_key, 2)
elif __ink_type == 'cmyk':
    k.tap_key(k.down_key, 2)
    #move to next slider
    k.tap_key(k.tab_key, 2)    


if __ink_type == 'cmykw' or __ink_type == 'w':
    #zero out    
    k.tap_key(k.home_key)
    #move highlight slider to 9
    k.tap_key(k.right_key, __highlight)
    #move to mask slider
    k.tap_key(k.tab_key, 1)
    
    # zero out
    k.tap_key(k.home_key)
    #move mask slider 
    k.tap_key(k.right_key, __mask)
    
    if __ink_type == 'cmykw':
        #move to background checkbox
        k.tap_key(k.tab_key)
        
        #check use black background
        if __use_background:
            k.tap_key(k.space)

elif __ink_type == 'cmyk':
    #zero out    
    k.tap_key(k.home_key)
    #move ink volumne
    k.tap_key(k.right_key, __ink_volumne)
    #move to dbl printing slider
    k.tap_key(k.tab_key)
    
    # zero out
    k.tap_key(k.home_key)
    #move dbl printing
    k.tap_key(k.right_key, __dbl_printing)     

if __ink_type != 'w':
#move to Color Pass
    k.tap_key(k.tab_key)   
    
    #check if needs multiple pass    
    if __multiple_pass:
        k.tap_key(k.space)
    
#move to advanced tab
k.tap_key(k.tab_key)        

#open advanced tab
k.tap_key(k.enter_key)  
#time.sleep(1)
#select transparent
if __transparent_color:
    if __ink_type == 'cmyk':
        
        msg_box = ctypes.windll.user32.MessageBoxW
        msg_box(None, 'CMYK can not have a transparent color setting, please check settigns', 'Error', 0)
        sys.exit(0)
    #check transparent color box
    k.tap_key(k.space)
    #move to custom
    k.tap_key(k.tab_key, 2)
    #open custom
    k.tap_key(k.enter_key)
    #time.sleep(1)
    #move to define colors
    k.tap_key(k.tab_key, 2)
    #open define colors
    k.tap_key(k.enter_key)
    #move to red    
    k.tap_key(k.tab_key, 3)
    
    ##enter numbers for custom red
    for c in range(len(__transparent_red)):
        k.tap_key(k.numpad_keys[int(__transparent_red[c])])
        
    #move to green
    k.tap_key(k.tab_key)
    
    ##enter numbers for custom green
    for c in range(len(__transparent_green)):
        k.tap_key(k.numpad_keys[int(__transparent_green[c])])
        
    #move to blue
    k.tap_key(k.tab_key)
    
    ##enter numbers for custom blue
    for c in range(len(__transparent_blue)):
        k.tap_key(k.numpad_keys[int(__transparent_blue[c])])

    #move back to the advanced tab
    k.tap_key(k.tab_key, 2)
    k.tap_key(k.enter_key)
    
    if __ink_type == 'cmykw' or __ink_type == 'w':
        #move to tolerance
        k.tap_key(k.tab_key)
        #adjust tolerance
        k.tap_key(k.home_key)
        k.tap_key(k.right_key, __tolorance)
    
    #move to next slider 
    k.tap_key(k.tab_key)
else:
    #move to next slider
    if __ink_type != 'cmyk':
        k.tap_key(k.tab_key)


  
#adjust min white    
if __ink_type == "cmykw":
    k.tap_key(k.home_key)
    k.tap_key(k.right_key, __min_white)

    #move to choke width
    k.tap_key(k.tab_key)

    #adjust choke
    k.tap_key(k.home_key)
    k.tap_key(k.right_key, __choke_width)

    #move to white color pause
    k.tap_key(k.tab_key)
    if __wht_color_pause:
        k.tap_key(k.space)
    
    #move to next slider
    k.tap_key(k.tab_key)
    
#zero out slider
k.tap_key(k.home_key)
k.tap_key(k.right_key, __saturation)

#move to brightness
k.tap_key(k.tab_key)

#change brightness
k.tap_key(k.home_key)
k.tap_key(k.right_key, __brightness)
   
#move to contrast
k.tap_key(k.tab_key)


#change contrast
k.tap_key(k.home_key)
k.tap_key(k.right_key, __contrast)

#move to unidirectional printing
k.tap_key(k.tab_key)

if __uni_printing:
    k.tap_key(k.space)

#close advanced

k.tap_key(k.enter_key)
   
#close printer properties
k.tap_key(k.tab_key, 2)
k.tap_key(k.enter_key)
    
 
 
#time.sleep(5)

#pause
time.sleep(1)
#move to print button
k.tap_key(k.tab_key, 17)
#click print button
k.tap_key(k.enter_key)
#pause 
time.sleep(10)
#click save on preview window

""" commented out so I can see the details """
k.tap_key(k.enter_key)
#pause
time.sleep(1)
#click save
k.tap_key(k.enter_key)
 #pause
time.sleep(1)
k.tap_key(k.enter_key)
 
open_word.kill()



