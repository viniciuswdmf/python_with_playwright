from features.page_objects.React.pages.login import *
from features.page_objects.React.pages.commons import *
from features.page_objects.React.pages.home import *
from features.page_objects.React.pages.movimentacao import *

class ReactIndex():

    def __init__(self, context):
        self.commons = ReactCommons(context)
        self.home = ReactHome(context)
        self.login = ReactLogin(context)
        self.movimentacao = ReactMovimentacao(context)

