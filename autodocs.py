import pyautogui
import time
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=438, y=375)
pyautogui.write("tiago@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=414, y=256)
    codigo = tabela.loc [linha, "codigo"]
    #codigo
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = tabela.loc [linha, "marca"]
    #marca
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = tabela.loc[linha , "tipo"]
    #tipo
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    #categoria
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    #preco_unitario
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    custo= tabela.loc[linha,"custo"]
    #custo
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    #obs 
    if not pandas.isna(obs):
        pyautogui.ite(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)