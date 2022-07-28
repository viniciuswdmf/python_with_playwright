from features.helper.page_helper import *
from features.page_objects.React.pages.components.el_home import *
from features.page_objects.React.pages.components.el_login import *
from features.page_objects.React.pages.components.el_movimentacao import *
from features.page_objects.React.pages.components.el_conta import *
from playwright.sync_api import expect
import time

class ReactConta():
    
    def __init__(self, context):
        pass

    def cadastrar_conta(self, context, conta):
        context.page.fill(conta_elements['INPUT_CONTA'], conta)
        context.page.click(conta_elements['BTN_SALVAR_CONTA']) 
        time.sleep(5)

    def validar_cadastro_conta(self, context):
        locator = context.page.locator(body_elements['TOAST_SUCESS'])
        expect(locator).to_be_visible()

    def excluir_conta(self, context):
        context.page.click(conta_elements['BTN_EXCLUIR_PRIMEIRA_CONTA'])
        time.sleep(2)

    def validar_exclusao_conta(self, context):
        locator = context.page.locator(body_elements['TOAST_SUCESS'])
        expect(locator).to_be_visible()


