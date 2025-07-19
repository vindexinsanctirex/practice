from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#abrir o navegador
navegador = webdriver.Chrome()

#acessar o site
navegador.get("https://www.mercadolivre.com.br/")

#testar em tela cheia
navegador.maximize_window()

#selecionar um elemento da tela
ofertas = navegador.find_elements("class name", "nav-menu-item-link")
for botao in ofertas:
    if "Ofertas" in botao.text:
        ofertas = botao
        break
ofertas.click()

#pesquisar um produto
navegador.find_element(By.NAME, "as_word").send_keys("celular")

#clicar no botão de buscar
botao_lupa = navegador.find_element(By.CLASS_NAME, "nav-icon-search")
botao_lupa.click()

#selecionar uma aba
abas = navegador.window_handles
navegador.switch_to.window(abas[0])

#navegar para um site diferente
navegador.get("https://www.mercadolivre.com.br/supermercado/market#nav-header")



time.sleep(10)