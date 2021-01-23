import pyautogui
import time
import win32api
import os


def listGacha():  # single phrase spam function
    startCount = int(input('Enter the starting ID for your gacha: '))
    endCount = int(input('Enter the last ID for your gacha: '))
    print("Click when you are ready to begin.")
    leftMouse = win32api.GetKeyState(0x01)
    mousePressed = False
    while mousePressed == False:
        changeInState = win32api.GetKeyState(0x01)
        if changeInState != leftMouse:  # Compare Previous and Current States
            mousePressed = True
            mPosX, mPosY = pyautogui.position()
        time.sleep(.01)
    # count = 1
    while startCount <= endCount:
        escKey = win32api.GetKeyState(0x1B)
        if escKey > 0:
            break
        pyautogui.click(mPosX, mPosY)  # get position of chatbox
        pyautogui.typewrite(".view " + str(startCount), interval=0.01)
        pyautogui.hotkey('enter')
        startCount += 1
        time.sleep(5)


def deleteGacha():
    print("Select where to list gachas")
    leftMouse = win32api.GetKeyState(0x01)
    mousePressed = False
    while mousePressed == False:
        changeInState = win32api.GetKeyState(0x01)
        if changeInState != leftMouse:  # Compare Previous and Current States
            mousePressed = True
            mPosX, mPosY = pyautogui.position()
        time.sleep(.01)
    pyautogui.typewrite(".list -low", interval=0.01)  # type user selected string, set interval time for typing each character
    pyautogui.hotkey('enter')
    print("Highlight the list")
    print(os.popen('xsel').read())


if __name__ == '__main__':
    selectWhatToDo = int(input('If you would like to list your gachas type 1\n'
                               'If you would like to start deleting your lowest gachas type 2: '))

    if selectWhatToDo == 1:
        listGacha()
    elif selectWhatToDo == 2:
        deleteGacha()
    else:
        pass
