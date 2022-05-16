import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.7

cont = 0

# ENCONTRAR PASTA
pyautogui.hotkey("win", "e")
pyautogui.click(x=540, y=101)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("backspace")
pyperclip.copy(r"A:\videos\PACK 500 ESTAMPAS INFANTIS\ARQUIVOS")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# ABRIR COREL
pyautogui.click(x=258, y=234, clicks=2)
pyautogui.click(x=2524, y=14)
time.sleep(6)

# EXPORTAR
pyautogui.hotkey("ctrl", "e")
pyautogui.click(x=1389, y=643)
pyautogui.click(x=2545, y=7)

# ENCONTRAR PASTA
pyautogui.hotkey("win", "e")
pyautogui.click(x=540, y=101)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("backspace")
pyperclip.copy(r"A:\videos\PACK 500 ESTAMPAS INFANTIS\ARQUIVOS")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# SELECIONAR ARQUIVO JÁ EXPORTADO
pyautogui.click(x=342, y=240)
pyautogui.hotkey("ctrl", "x")
pyautogui.click(x=230, y=212, clicks=2)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("alt", "f4")

cont = cont - 1
print(cont)
