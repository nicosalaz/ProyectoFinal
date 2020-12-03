from behave import *
from selenium import webdriver
from time import sleep
import random
import comprar_sin_logguearse as csl

@given('ya se haya iniciado el browser.')
def iniciar_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()



@given('este en la pagina de registrar.')
def register_page(context):
    context.driver.get('http://localhost:8000/Tienda/Registrar/')


@when('Escribe cedula "{cedula}"')
def escribir_ced(context,cedula):
    context.driver.find_elements_by_xpath("//input[@id='id_identificacion']")[0].send_keys(cedula)
    sleep(random.uniform(2,4))


@when('Escribe nombre "{nom}"')
def escribir_nom(context,nom):
    context.driver.find_elements_by_xpath("//input[@id='id_nombre']")[0].send_keys(nom)
    sleep(random.uniform(2, 4))


@when('Escribe apellido "{ape}"')
def escribir_ape(context,ape):
    context.driver.find_elements_by_xpath("//input[@id='id_apellido']")[0].send_keys(ape)
    sleep(random.uniform(2, 4))



@when('Escribe telefono "{tel}"')
def escribir_tel(context,tel):
    context.driver.find_elements_by_xpath("//input[@id='id_telefono']")[0].send_keys(tel)
    sleep(random.uniform(2, 4))


@when('Escribe direccion "{dir}"')
def escribir_dir(context,dir):
    context.driver.find_elements_by_xpath("//input[@id='id_direccion']")[0].send_keys(dir)
    sleep(random.uniform(2, 4))


@when('Escribe Fecha "{fecha}"')
def escribir_fecha(context,fecha):
    context.driver.find_elements_by_xpath("//input[@id='id_fecha_nacimiento']")[0].send_keys(fecha)
    sleep(random.uniform(2, 4))


@when('escribe Usuario "{usu}"')
def escribir_usu(context,usu):
    context.driver.find_elements_by_xpath("//input[@id='id_usuario']")[0].send_keys(usu)
    sleep(random.uniform(2, 4))

@when('Escribe clave "{pwd}"')
def escribir_pwd(context,pwd):
    context.driver.find_elements_by_xpath("//input[@id='id_password']")[0].send_keys(pwd)
    sleep(random.uniform(2, 4))


@when('se oprime el boton registrar')
def register_button(context):
    context.driver.find_elements_by_xpath("//button[contains(text(),'Crear Cuenta')]")[0].click()
    sleep(random.uniform(2, 4))


@then('se crea el usuario y se redirecciona a la página del login')
def register_verify(context):
    csl.verificar_logo(context)
