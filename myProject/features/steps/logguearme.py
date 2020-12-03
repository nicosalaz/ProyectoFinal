from behave import *
from selenium import webdriver
import random
from time import sleep
import comprar_sin_logguearse as cp

@given('Ya se inicio el browser.')
def login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://localhost:8000/accounts/login/')
    context.driver.maximize_window()
    sleep(random.uniform(2,4))


@given('Esta en la pagina del login.')
def verif_logo(context):
    cp.verificar_logo(context)
    sleep(random.uniform(2, 4))

@when('Ingresa el usuario "{usuario}" e ingresa la contraseña "{pwd}".')
def ingresar_usuario(context,usuario,pwd):
    context.driver.find_elements_by_xpath('//input[@id="id_username"]')[0].send_keys(usuario)
    context.driver.find_elements_by_xpath('//input[@id="id_password"]')[0].send_keys(pwd)
    sleep(random.uniform(2, 4))


@when('presiona al boton Iniciar sesion.')
def ingresar(context):
    context.driver.find_elements_by_xpath('//button[contains(text(),"Iniciar Sesión")]')[0].click()
    sleep(random.uniform(2, 4))


@then('aparece su nickname con un mensaje de bienvenida.')
def verificar_user(context):
    texto = context.driver.find_element_by_xpath("//body/div[@id='layoutSidenav']/div[@id='layoutSidenav_nav']/nav[@id='sidenavAccordion']/div[1]/div[1]/a[1]").text
    assert  texto == 'Bienvenido nicosalaz'

