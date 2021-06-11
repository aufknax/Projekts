import pyautogui, time

adressed_to ='Taschler'
message = 'jo'



pyautogui.moveTo(112, 154)
time.sleep(3)
pyautogui.doubleClick()
time.sleep(4)
pyautogui.moveTo(100, 125, 0.25)
pyautogui.click(); pyautogui.write(adressed_to)
pyautogui.moveTo(171, 247)
time.sleep(2)
pyautogui.doubleClick()


time.sleep(3)
pyautogui.moveTo(610, 1013)

for i in range(10000):
     pyautogui.write(message)
     pyautogui.press('enter')

for i in range(100):
    time.sleep(0.2)
    print(pyautogui.position())



