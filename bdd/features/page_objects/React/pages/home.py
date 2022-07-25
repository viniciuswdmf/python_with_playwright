from features.helper.page_helper import *
from features.page_objects.React.pages.components.el_home import *
from features.page_objects.React.pages.components.el_login import *
from playwright.sync_api import expect
import time

class ReactHome():
    
    def __init__(self, context):
        pass

    def acessar_movimentacao(self, context):
        context.page.click(body_elements['MENU_MOVIMENTACAO']) 
        time.sleep(5)