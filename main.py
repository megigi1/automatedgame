# Time to start this game!
# Name of it : Automate Dinosaur Game
# Taking picture to equal to pixels by screenshot
# When pixels are ok, then robot automaticcly starts running
# Manage to robot to jump automaticly

import pyautogui
from PIL import Image, ImageGrab

import time


def click(key):
    pyautogui.keyDown(key)
    return


def isCollision(data):
    # Check colison for birds
    for i in range(530, 560):
        for j in range(80, 127):
            if data[i, j] < 171:
                click("down")
                return
    # Check colison for cactus
    for i in range(530, 620):
        for j in range(130, 160):
            if data[i, j] < 100:
                click("up")
                return
    return


if __name__ == "__main__":
    time.sleep(5)
    click('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollision(data)
