import random
from time import sleep
from behave import *
from selenium import webdriver


@given('que estas en la pagina principal')
def home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://localhost:8000/Indexlog/')
    context.driver.maximize_window()
    sleep(random.uniform(2, 4))


@given('no esta el nombre de tu usuario en la bienvenida')
def nombre_user(context):
    nombre = context.driver.find_elements_by_xpath("//body/div[@id='layoutSidenav']/div[@id='layoutSidenav_nav']/nav[@id='sidenavAccordion']/div[1]/div[1]/a[1]")[0].text
    assert nombre == 'Bienvenido AnonymousUser'

@when('agregas un producto al carrito de compra')
def agregar_al_carrito(context):
    context.driver.find_elements_by_xpath('//a[@class="small text-black stretched-link"]')[0].click()
    sleep(random.uniform(2, 4))

@then('te envia a la pagina del login y ves el logo de Login.')
def verificar_logo(context):
    logo = context.driver.find_element_by_xpath('//h3[contains(text(),"Login N & JD")]').text
    assert logo == "Login N & JD"
    sleep(random.uniform(2, 4))

@then('se cierra el browser.')
def close_browser(context):
    context.driver.close()
