from behave import *
from selenium import webdriver
from time import sleep
import random
import logguearme as lg

@given('Ya se inció el browser.')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8000/accounts/login/")
    context.driver.maximize_window()
    sleep(random.uniform(2,4))

@given('se loggeó correctamente.')
def loggearse(context):
    lg.ingresar_usuario(context,'nicosalaz','n1c0l4s10')
    lg.ingresar(context)
    sleep(random.uniform(2, 4))

@given('estas en catalogo de productos.')
def cat_productos(context):
    catalogo = context.driver.find_elements_by_xpath("//h1[contains(text(),'Productos')]")[0].text
    assert catalogo == "Productos"
    sleep(random.uniform(2, 4))

@given('Seleccionas un producto.')
def agregar_carrito(context):
    context.driver.find_elements_by_xpath("//button[@type='submit']")[1].click()
    sleep(random.uniform(2, 4))



@given('Se da click en el boton para ir al carrito.')
def ir_al_carrito(context):
    context.driver.find_elements_by_xpath("//body/div[@id='layoutSidenav']/div[@id='layoutSidenav_nav']/nav[@id='sidenavAccordion']/div[1]/div[1]/div[2]/a[1]")[0].click()
    sleep(random.uniform(2, 4))


@given('se visualiza el producto seleccionado en carrito.')
def visualizar_carrito(context):
    letrero = context.driver.find_elements_by_xpath("//h1[contains(text(),'Tu carrito de compra nicosalaz')]")[0].text
    assert letrero == 'Tu carrito de compra nicosalaz'
    sleep(random.uniform(2, 4))

@when('se de click en el boton de filizar comprar')
def finalizar_compra(context):
    context.driver.find_elements_by_xpath("//button[contains(text(),'Finalizar Compra')]")[0].click()
    sleep(random.uniform(2, 4))


@then('se realizara la compra y te mostrará el total a pagar.')
def factura(context):
    fac = context.driver.find_elements_by_xpath("//h1[contains(text(),'Factura De Compra')]")[0].text
    assert fac == 'Factura De Compra'
    sleep(random.uniform(2, 4))

