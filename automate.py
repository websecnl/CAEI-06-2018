import pyautogui
import os
import time
import subprocess
from win32api import GetSystemMetrics

# Coded for: Chrome Version 66.0.3359.117 (Official Build)
# Supported Resolutions: 1920x1080,1280x800,1600x900,1366x768,1440x900

CHROME_STAUTS = False
MoniH = GetSystemMetrics(0)
MoniW = GetSystemMetrics(1)
Res   = (str(MoniH) + 'x' + str(MoniW))
s = subprocess.check_output('tasklist', shell=True)

def kill_chrome():
    print '[+] Killing Chrome Instances...'
    print ""
    print '[------DEBUG_LOG------]'
    os.system("taskkill /im chrome.exe")
    print '[---------------------]'
    print ""

if "chrome.exe" in s:
    print '[!] Hmm, Chrome Is Running'
    print '[+] Killing Chrome Instances...'
    print ""
    print '[------DEBUG_LOG------]'
    kill_chrome()
    print '[---------------------]'
    print ""
    print '[+] Done'
    CHROME_STAUTS = True
else:
    print '[+] All Good, Chrome Is Not Running.'
    CHROME_STAUTS = False

def automate():
    time.sleep(1)
    # From here everything is based on Resolution unfortunatley
    if Res == '1920x1080':
        print ('[+] Using: ' + Res)
        pyautogui.click(275, 46)
        pyautogui.press('delete')
        pyautogui.click(275, 46)
        time.sleep(1)
        pyautogui.typewrite('javascript:document.getElementsByClassName("g-c-R webstore-test-button-label")[0].click();')
        time.sleep(1.5)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(964, 208, clicks=1, button='left')
        time.sleep(1)
        pyautogui.press('escape')
        # Hides from Menu
        pyautogui.click(1862, 45, button='right')
        pyautogui.click(1781, 168)
        # Kill Chrome
        kill_chrome()
    elif Res == '1280x800':
        print '[+] Using: ' + Res
        pyautogui.click(275, 46)
        pyautogui.press('delete')
        pyautogui.click(275, 46)
        time.sleep(1)
        pyautogui.typewrite('javascript:document.getElementsByClassName("g-c-R webstore-test-button-label")[0].click();')
        time.sleep(1.5)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(639, 209, clicks=1, button='left')
        time.sleep(1)
        pyautogui.press('escape')
        # Hides from Menu
        pyautogui.click(1223, 47, button='right')
        pyautogui.click(1128, 159)
        # Kill Chrome
        kill_chrome()
    elif Res == '1600x900':
        print '[+] Using: ' + Res
        pyautogui.click(275, 46)
        pyautogui.press('delete')
        pyautogui.click(275, 46)
        time.sleep(1)
        pyautogui.typewrite('javascript:document.getElementsByClassName("g-c-R webstore-test-button-label")[0].click();')
        time.sleep(1.5)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(802, 211, clicks=1, button='left')
        time.sleep(1)
        pyautogui.press('escape')
        # Hides from Menu
        pyautogui.click(1540, 46, button='right')
        pyautogui.click(1443, 156)
        # Kill Chrome
        kill_chrome()
    elif Res == '1366x768':
        print '[+] Using: ' + Res
        pyautogui.click(275, 46)
        pyautogui.press('delete')
        pyautogui.click(275, 46)
        pyautogui.typewrite('javascript:document.getElementsByClassName("g-c-R webstore-test-button-label")[0].click();')
        time.sleep(1.5)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(686, 209, clicks=1, button='left')
        time.sleep(1)
        pyautogui.press('escape')
        # Hides from Menu
        pyautogui.click(1305, 44, button='right')
        pyautogui.click(1216, 155)
        # Kill Chrome
        kill_chrome()
    elif Res == '1440x900':
        print '[+] Using: ' + Res
        pyautogui.click(275, 46)
        pyautogui.press('delete')
        pyautogui.click(275, 46)
        time.sleep(1)
        pyautogui.typewrite('javascript:document.getElementsByClassName("g-c-R webstore-test-button-label")[0].click();')
        time.sleep(1.5)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(755, 209, clicks=1, button='left')
        time.sleep(1)
        pyautogui.press('escape')
        # Hides from Menu
        pyautogui.click(1382, 47, button='right')
        pyautogui.click(1294, 155)
        # Kill Chrome
        kill_chrome()
    else:
        print 'Error'
if CHROME_STAUTS == 'True':
    os.system ('start chrome.exe https://chrome.google.com/webstore/detail/jquery-adder-v2/mlfcfehhdkhpddndcnlaedioadfefpcd --start-maximized')
    # Code should come here that closes the chrome notification of 'Chrome not closed correctly, restore?'
    time.sleep(0.5)
    automate()
else:
    os.system('start chrome.exe https://chrome.google.com/webstore/detail/jquery-adder-v2/mlfcfehhdkhpddndcnlaedioadfefpcd --start-maximized')
    time.sleep(0.5)
    automate()
