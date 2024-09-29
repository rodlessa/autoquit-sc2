import pyautogui
import cv2
import numpy as np
import time

play_image = cv2.imread('play_image.png')
second_image = cv2.imread('second_image.png')
score_image = cv2.imread('score_image.png')
button_image = cv2.imread('play_again.png')

def detect_button(image, threshold=0.8):
    screenshot = pyautogui.screenshot()
    
    screen_np = np.array(screenshot)
    screen_rgb = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)
    
    result = cv2.matchTemplate(screen_rgb, image, cv2.TM_CCOEFF_NORMED)
    
    loc = np.where(result >= threshold)
  
    for pt in zip(*loc[::-1]):
        return pt  
    
    return None

while True:
    play_image_position = detect_button(play_image)
    if play_image_position:
        print('Status: Starting match     ', end="\r")
        pyautogui.click(play_image_position)
        time.sleep(1)  
        print('Status: Match started      ', end="\r")  # Sobrescreve a linha anterior
    second_image_position = detect_button(second_image)
    if second_image_position:
        pyautogui.press('f10')
        pyautogui.press('n')
        print('Status: Quitting           ', end="\r")
    score_image_position = detect_button(score_image)
    if score_image_position:
        pyautogui.press('s')
        time.sleep(1)
        print('Status: Opponent quit, Win!', end="\r")
    button_position = detect_button(button_image)
    if button_position:
        pyautogui.click(button_position)
        print('Status: Queueing!', end="\r")
    time.sleep(1)
