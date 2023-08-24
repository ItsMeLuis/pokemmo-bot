import mss.tools
import pyautogui as pag
import Quartz.CoreGraphics as cg # Pegar as coordenadas da tela do jogo
import cv2 as cv
import numpy as np
import pyautogui as pag
from time import sleep
import subprocess


SCALE = 0.5 # Scala * 2 para bater o tamanho do Liquid Retina Display


def open_game():
    subprocess.call(
        ["/usr/bin/open", "-n", "-a", "/Applications/PokeMMO.app"]
        )
    sleep(3)
    pag.hotkey('tab')
    pag.hotkey('tab')
    pag.hotkey('space')
    sleep(3)
    pag.hotkey('space')
    sleep(2)
    pag.hotkey('space')
    sleep(2)
    pag.hotkey('space')


def game_coords():
    # Obtém uma lista de todas as janelas ativas
    windows = cg.kCGWindowListOptionOnScreenOnly | cg.kCGWindowListExcludeDesktopElements
    window_list = cg.CGWindowListCopyWindowInfo(windows, cg.kCGNullWindowID)
    # print(window_list)
    for window_info in window_list:
        if window_info[cg.kCGWindowOwnerName] == 'java':
            bounds = window_info[cg.kCGWindowBounds]
            left = bounds['X']
            top = bounds['Y']
            right = left + bounds['Width']
            bottom = top + bounds['Height']
            return int(left), int(top), int(right), int(bottom)
    return None


def captureGameScreen(left, top, right, bottom):
    top *= SCALE
    left *= SCALE
    width = (left - right) * SCALE
    heigth = (bottom - top) * SCALE
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": top, "left": left, "width": width, "height": heigth}
        output = "img/gameScreen.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)


def locate(img):
    try: 
        a = pag.locateOnScreen('./img/'+img+'.png', confidence=0.8)
    except Exception as Ex:
        a = Ex
    return a


def searchCapture(img):
    a = locate(img)
    captureGameScreen(a[0], a[1], a[2], a[3])


def readPokemonName(pokeName):
    #Tirar print da tela do jogo (ver se é possível ver onde o jogo está posicionado e printar apenas aquela regiao)

    # Com OpenCV identificar se o nome do pokemon encontrado é igual ao nome do pokemon desejado

    # Se for, retorna que True, se não for, retorna False
    return 0