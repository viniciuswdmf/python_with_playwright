from features.helper.page_helper import *
from features.page_objects.React.pages.components.el_home import *
from features.page_objects.React.pages.components.el_login import *
from features.page_objects.React.pages.components.el_movimentacao import *
from features.page_objects.React.pages.components.el_extrato import *
from playwright.sync_api import expect
import time

class ReactExtrato():
    
    def __init__(self, context):
        pass

    def selecionar_primeira_movimentacao(self, context):
        context.page.click(extrato_elements['ALTERAR_PRIMEIRO_ITEM'])
        time.sleep(5)

    def excluir_primeira_movimentacao(self, context):
        context.page.click(extrato_elements['EXCLUIR_PRIMEIRO_ITEM'])
        time.sleep(3)

    def validar_exclusao_primeiro_item(self, context):
        locator = context.page.locator(body_elements['TOAST_SUCESS'])
        expect(locator).to_be_visible()


