import pyautogui, time
time.sleep(5)

file = open("send.txt", "r")

for word in file:
    # print(word)
    pyautogui.typewrite(word)
    pyautogui.press("enter")