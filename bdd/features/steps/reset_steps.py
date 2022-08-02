from behave import given, when , then
import time

@when(u'clicar no menu referente a opcao reset')
def resetando_informacoes(context):
    context.react.home.resetar_infos(context)


@then(u'o site deve ser resetado')
def validando_acao_reset(context):
    context.react.home.validar_reset(context)