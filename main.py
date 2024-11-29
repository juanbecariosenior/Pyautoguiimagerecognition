from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(1)

"""con este comando puedes ver la posicion en X y Y 
del mouse, tambien el color rgb del pixel donde estas 
posicionado"""
#pyautogui.displayMousePosition() 

"""Para este primer progrma obten el lugar de 
los pixeles donde se encuentran las primeras teclas
para eso utiliza el comando de abajo"""

"""
Este código define una función en Python llamada 
click que simula un clic izquierdo del mouse en 
una posición específica de la pantalla
"""
def click(x,y):
    win32api.SetCursorPos((x,y)) #Mueve el cursor del mouse a las coordenadas (x, y) en la pantalla
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #Simula el evento de "presionar" el botón izquierdo del mouse
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #Simula el evento de "soltar" el botón izquierdo del mouse

"""
Este fragmento de código implementa un bucle que continuamente verifica 
el color de ciertos píxeles en la pantalla. Si el valor del canal rojo 
del píxel coincide con uno de los valores especificados (0, 16, 17), 
simula un clic en la posición correspondiente. 
El bucle se detiene cuando el usuario presiona la tecla 'q'
"""
while keyboard.is_pressed('q') == False: # Mientras no se presione la tecla 'q':
    if pyautogui.pixel(441,853)[0] in (0,16,17): #Si el valor del canal rojo del píxel en (441, 853) es 0, 16 o 17
        click(441,853) # Realiza un clic en la posición (441, 853)
    if pyautogui.pixel(578,851)[0] in (0,16,17):
        click(578,851)
    if pyautogui.pixel(724,839)[0] in (0,16,17):
        click(724,839)
    if pyautogui.pixel(865,842)[0] in (0,16,17):
        click(865,842)