from features.helper.page_helper import *
from features.page_objects.React.pages.components.el_home import *
from features.page_objects.React.pages.components.el_login import *
from playwright.sync_api import expect
import time

class ReactLogin():
    
    def __init__(self, context):
        pass

    def acessar_site_login(self, context):
        context.page_helper.acessar(context, "")

    def fazer_login_com_parametros(self, context, cpf, senha):
        context.page.fill(login_elements['INP_LOGIN'], cpf)
        context.page.fill(login_elements['INP_SENHA'], senha)
        context.page.click(login_elements['INP_BTN_LOGIN']) 
        time.sleep(5)

    def validar_login_correto(self, context):
        locator = context.page.locator(body_elements['TOAST_SUCESS'])
        expect(locator).to_be_visible()

