from features.helper.page_helper import *
from features.page_objects.React.pages.components.el_home import *
from features.page_objects.React.pages.components.el_login import *
from features.page_objects.React.pages.components.el_movimentacao import *
from playwright.sync_api import expect
import time

class ReactMovimentacao():
    
    def __init__(self, context):
        pass

    def cadastrar_movimentacao(self, context, descricao, valor, interessado, conta):
        context.page.fill(movimentacao_elements['DESCRICAO'], descricao)
        context.page.fill(movimentacao_elements['VALOR'], valor)
        context.page.fill(movimentacao_elements['INTERESSADO'], interessado)
        context.page.locator(movimentacao_elements['CONTA_ALTERAR']).select_option(value=conta)
        context.page.click(movimentacao_elements['BOTAO_SALVAR']) 
        time.sleep(5)

    def validar_cadastro_movimentacao(self, context):
        locator = context.page.locator(body_elements['TOAST_SUCESS'])
        expect(locator).to_be_visible()

