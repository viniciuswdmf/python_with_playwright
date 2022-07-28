from features.helper.page_helper import *
from features.page_objects.React.pages.components.el_home import *
from features.page_objects.React.pages.components.el_login import *
from features.page_objects.React.pages.components.el_conta import *
from playwright.sync_api import expect
import time

class ReactHome():
    
    def __init__(self, context):
        pass

    def acessar_movimentacao(self, context):
        context.page.click(body_elements['MENU_MOVIMENTACAO']) 
        time.sleep(5)
    
    def acessar_extrato(self, context):
        context.page.click(body_elements['MENU_EXTRATO'])
        time.sleep(5)

    def acessar_conta(self, context):
        context.page.click(body_elements['DROPDOWN_MENU'])
        time.sleep(3)
        context.page.click(body_elements['MENU_CONTA'])
        time.sleep(5)

    def acessar_registro(self, context):
        context.page.click(body_elements['MENU_REGISTRO'])