"""
Aqui no page_helpers é possível criar funções que podem ser reutilizadas
varias vezes dentro dos mapeamentos dos sistemas no page_objects
caso tenha alguma função de validação por exemplo, que serve tanto para um sistema quanto para outro.

"""
from features.page_objects.React.react_page_index import *


class PageHelper():

    def __init__(self, context):
        pass

    def acessar(self, context, url_complemento):
        context.ambiente = context.config.userdata["ambiente"]
        context.url_dev = "https://barrigareact.wcaquino.me/"
        context.url_stage = "https://barrigareact.wcaquino.me/"
        context.url_prod = "https://barrigareact.wcaquino.me/"

        if context.ambiente == "dev":
            context.page.goto(context.url_dev+url_complemento)

        elif context.ambiente == "stage":
            context.page.goto(context.url_stage+url_complemento)

        elif context.ambiente == "prod":
            context.page.goto(context.url_prod+url_complemento)
            
        else:
            print("Digite o ambiente!")