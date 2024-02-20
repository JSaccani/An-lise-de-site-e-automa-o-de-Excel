from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# acessar site:
driver = webdriver.Chrome()
driver.get("https://www.novaliderinformatica.com.br/computadores-gamers")


# extrair título:
titles = driver.find_elements(By.XPATH,'//a[@class="nome-produto"]')

# extrair todos os preços:
prices = driver.find_elements(By.XPATH,'//strong[@class="preco-promocional"]')

# criar planilhas:
workbook = openpyxl.Workbook()
workbook.create_sheet("produtos")
sheet_produtos = workbook["produtos"]
sheet_produtos["A1"].value = "Products"
sheet_produtos["B1"].value = "Prices"


for title, price in zip(titles, prices):
    sheet_produtos.append([title.text, price.text])

workbook.save("produtos.xlsx")
