from behave import given, when, then
import time

@when(u'realizar login com CPF e senha válidos')
def realizar_login_teste(context):
    context.react.login.acessar_site_login(context)
    context.react.login.fazer_login_com_parametros(context, "tarcisio@cy.com", "1")


@then(u'deve validar que o login foi realizado com sucesso')
def verificar_login(context):
    context.react.login.validar_login_correto(context)