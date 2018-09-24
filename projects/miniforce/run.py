#!/usr/bin/env python

import colorsys
import time
import base64

#Load blinkt module
import blinkt
blinkt.set_clear_on_exit()
blinkt.set_brightness(0.1)

#Character dictionary with rgb values
characters = {'volt': [0,0,255], #blue
             'lucy': [255,0,127], #pink
             'sammy': [255,0,0], #red
             'max': [255,255,0], #yellow
             'ray': [0,0,0], #black
             'hawk': [61,145,64], #green
             'anna': [255,255,255], #white
             'mommy': [160,32,240], #medium purple
             'daddy': [131,137,150], #roman silver
             'athena': [0,201,87], #emerald green
            }

def rainbow():
    spacing = 360.0 / 16.0
    hue = 0
    count = 0

    while count < 200:
        hue = int(time.time() * 100) % 360
        for x in range(8):
            offset = x * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            blinkt.set_pixel(x, r, g, b)
        blinkt.show()
        time.sleep(0.001)
        count = count + 1

def display_color(name):
    blinkt.clear()

    #Rainbow if name is penny
    if name in ['penny', 'Penny', 'PENNY']:
        print ("Hello Penny!")
        rainbow()
    #Otherwise perform name lookup
    elif name in list(characters.keys()):
        print ("Miniforce Transform!")
        #Set color
        r, g, b = [int(x) for x in characters.get(name)]
        for i in range(8):
            blinkt.set_pixel(i, r, g, b)
            blinkt.show()
    #Clear and quit
    else:
        print("Thank you for using Miniforce color lookup!")
        exit(0)

#Miniforce logo in base64
logo = "Li4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLgouLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uCi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4sPyUlPzsuLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4KLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uOysqU1M/JSUrLCwuLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLgouLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLjo/Pzs6Ojo6Ojo6OjolOiw6LC4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uCi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4/JTo6Ojo6OioqOjo6OjolOlM6Li4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4KLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uPys6Ojs7Ojo6Ojo/Uzo6OjolPyU6Li4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLgouLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi47Li4uLi4uLFNTJSU6OipTU1NTJTs6JVMrOiwlOj8uLi4uLi4uLi4uLi4uLi47Oi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uCi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uOiosLi4uLi4qOjsqOytTU1NTJSUlU1M6JVM6Oz8qOjsuLi4uLi4uLi4uLi4uLioqKywuLi4uLi4uLi4uLi4uLi4uLi4uLi4KLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4rUyo7LCwsLDo/Kz9TJSorKzssLi4uOisrKio/Pz8rPzosLCwuLi4uLi4uLi4uPyUrKissLi4uLi4uLi4uLi4uLi4uLi4uLgouLi4uLi4uLi4uLi4uLi4uLi4uLi4uLiw6Ojs7Kz9TUyorKioqKio/P1NTJVMlKisqOzorJSVTJVM/Pz8/PyoqKysrKzsrOzs7Ojo7Uz8qJSs6Li4uLi4uLi4uLi4uLi4uLi4uCi4uLi4uLC4uLi4uLDo7KysrKysqKj8/JSVTU1NTUzsqUz8/UyMrIyorU1MqKyUlJSoqPyU/PysqUysrKyojKysqKlMjJVNTU1MlJT8/KipTJT8rKysrOzosLi4uLi4uLi4uLi4KLi4uLi4sOzsrKysrKiolU1NTU1NTJSorUzosOlMrK1NTKiolJSpTKipTUysrJSsqJT8/KiUqKz9TKiolPyMqKj8qK1MqOzosOlMqKyo/JVNTJSNTUyU/KisrKysrOywuLi4uLgouLi4uLjslJSUlPys7KyolU1MlKiorOiMuLDolUysqUyoqKj8/P1M/P1NTPyVTPysrOysrJT8lU1M/PyVTU1M/JVMqP1MrKlM6O1MrJVMlP1M/JSUlJSUlI1MrKz8lJS4uLi4uCi4uLi4uLCUlJSUlJSUlKjsrUzs6Kzo/Ozs6OlMrOiUqO1M6Ozs/JTsrU1MlK1MqJTs7KiVTKz9TUys7Ozs6Iyo7U1M6JTosUz8sUyo6U1M7Kj87KiolU1MqKyUlJSU7Li4uLi4KLi4uLi4uLi4sOiolJSU6Uz8sLj86Oy46OyxTPy47UywuIywuLlM6Lj9TUyUsPyUrPzorPz86O1NTPy4uU1NTUy47UywsUy4sLC4sUy46U1MjIzosPyM/O1NTJSU7Li4uLi4uLgouLi4uLi4uLi4uLi47OyMrLCw6PywuO1MuLFMsLFNTLDpTOyw6IywsJVNTUywrPzolJSs6KywqU1MlLCwjU1NTOjpTKyxTKiwlLCtTOyxTIzslUzo6JSMlKiUsLi4uLi4uLi4uCi4uLi4uLi4uLi4uLDtTKzo6O1M6OjtTPywlKjosUzs6JVMqOisjOztTU1NTOyxTOy4sLiUsLCVTU1MrK1NTU1NTOzo6Oj9TOj9TOiVTOjtTKjsjOzs7K1MrOy4uLi4uLi4uLi4KLi4uLi4uLi4uLjsrUzs7OzsjJTsrU1M/JVNTU1NTU1NTU1MlJSU/KioqKiolJTs/Oi4lOyUlPyoqKioqPz8lJSUlJVNTU1NTU1NTJSNTPys7Oz8lOzs/JSNTOywuLi4uLi4uLgouLi4uLi4uLi47KiM7Ozs7IyMjU1MlJT8/KisrKzsrKysrKiorKysrOzsrPys/JSVTPyVTKisqPyoqKysrKioqKiorKzsrKysrKio/JSVTU1MjIyMrKytTIyM/KywuLi4uLi4uCi4uLi4sLi47K1MrOjo6KiMlKiorKzs7OiwsLCwsLi4uLi4uLi4uLi4sLDoqKioqKioqKyo/Pz8qKjs7Ojo7Ojs7OzsrKysrKysrKyoqKio/KioqPyM6OjojIyNTKiwuLi4uLi4KLi4uLi4uOitTPzsrKysjPyo7Ojo6OjosLCwsLCwsLCwsOjo6Ojo6OjorKz8qKisqOjoqKj8qPyU/Ozs6Kzs7OysrKysrKysrKysqKioqKioqKj8qUyUqKyorKj8jKywuLi4uLgouLi4uLio/UyUlJVMjIz8lJT8rOzs6OiwsLi4uLi4uLi4uLi4sKiw7OiolK1NTKyssOioqLC4rUzs6OiouLi4uLi4uLi4uLi4uLiwsOjsrKioqJSU/IyMjU1MlJSUjPzouLi4uCi4uLiwqJSMjIyNTJSU/JSUlOy4uLi4uLi4uLi4uLi4uLi4uLi4sOzoqOiUlU1NTJTo6OiwqU1NTJTo/OiosLi4uLi4uLi4uLi4uLi4uLi4uLi4qUz8/PyVTUyMjIyMjPzsuLC4KLi4qPz8/Pz8/PyorOzslJTsuLi4uLi4uLi4uLi4uLi4uLi4uLiwlOlMqOjo7U1M7KyVTU1MlKzorJVNTLC4uLi4uLi4uLi4uLi4uLi4uLi4uLi4lKioqKj8/Pz8/Pz8lJT8uLgouOz8/KioqKysrKys7Oz8rLi4uLi4uLi4uLi4uLi4uLi4uLi4uLiwlP1MrOjo7JVM6Ojo6Ojo7JSo6JSosLi4uLi4uLi4uLi4uLi4uLi4uLi4uLj8qKioqPz8/Pz8/Pz8/PysuCi4qKioqKioqKisrKzs7LC4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLjpTOlM6Ojo6OioqOjo6Ojo6OiU6Li4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLDo6Kyo/Pz8/Pz8/Pz8lOy4KLiwqKzs6LC4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLjo/LCUlOjo6Ozo6Ojo7Pz86Li4sLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLDorKj8uLgouLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLCpTPyslU1MlPyssLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4sLi4uCi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uOjs7OywuLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4KLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLi4uLgo="

print(base64.b64decode(logo))
while True:
    #Get character name
    display_color(raw_input('Miniforce to dispatch: '))
