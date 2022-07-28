import pyautogui as py
import pyperclip
import time
import pandas as pd

py.PAUSE = 1
py.hotkey("alt", "tab")
py.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
py.hotkey("ctrl", "v")
py.press("enter")
time.sleep(5)

#Point(x=525, y=338)
py.click(x=525, y=338, clicks=2)
time.sleep(2)

py.click(x=525, y=338, button="right")
time.sleep(2)

#Point(x=700, y=909)
py.click(x=700, y=909)

time.sleep(5)


tabela = pd.read_excel(r"C:\Users\levir\Downloads\Vendas - Dez.xlsx")
print(tabela)

quantidade = tabela["Quantidade"].sum() #soma da coluna quantidade

faturamento = tabela["Valor Final"].sum() #soma da coluna valor final

print(f"{quantidade} unidades vendidas")

print(f"R${faturamento} de faturamento da somatoria de todas as lojas")

#entrar no email de forma automática
#Relatório de Vendas    py.hotkey("alt","tab")
py.hotkey("ctrl","t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
py.hotkey("ctrl","v")
py.press("enter")
time.sleep(8)


#mandar um email
#clicar no botão mais
#Point(x=69, y=193)
py.click(x=69, y=193)
time.sleep(2)
#escrever o destinatário
py.write("marianadbueno1507@gmail.com")
py.press("tab")
py.press("tab")

#escrever o assunto
pyperclip.copy("Relatório de Vendas")
py.hotkey("ctrl","v")
py.press("tab")

#escrever o corpo do email
texto = f"""Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f} 
A quantidade de produtos vendidos foi de: {quantidade:,} itens

Abs
Levir Menezes"""
pyperclip.copy(texto)
py.hotkey("ctrl", "v")

#enviar email
py.hotkey("ctrl","enter")
