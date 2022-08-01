from features.helper.page_helper import *
from features.page_objects.React.pages.components.el_home import *
from features.page_objects.React.pages.components.el_login import *
from features.page_objects.React.pages.components.el_registro import *
from playwright.sync_api import expect
import time

class ReactRegistro():
    
    def __init__(self, context):
        pass

    def registrar_com_parametros(self, context, nome, email, senha):
        context.page.fill(registro_elements['INP_NOME'], nome)
        context.page.fill(registro_elements['INP_EMAIL'], email)
        context.page.fill(registro_elements['INP_SENHA'], senha)
        context.page.click(registro_elements['BTN_REGISTRO']) 
        time.sleep(5)

    def validar_registro_correto(self, context):
        locator = context.page.locator(body_elements['TOAST_SUCESS'])
        expect(locator).to_be_visible()

