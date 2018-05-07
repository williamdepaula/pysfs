from selenium import webdriver

navegador = webdriver.Firefox()
navegador.get('http://localhost:5000')

assert 'Olá Mundo!' in navegador.title
