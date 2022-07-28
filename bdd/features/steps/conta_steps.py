from behave import given, when, then

@given(u'que tenha acessado a pagina de conta')
def acessar_menu_conta(context):
    context.react.home.acessar_conta(context)
    

@when(u'preencher o nome da conta')
def preencher_nome_conta(context):
    context.react.conta.cadastrar_conta(context, "Conta bzuubzu")


@then(u'a conta deve ser cadastrada')
def validar_conta_nova(context):
    context.react.conta.validar_cadastro_conta(context)

    #################excluir

@when(u'clicar em excluir a primeira conta')
def excluir_primeira_conta(context):
    context.react.conta.excluir_conta(context)


@then(u'a conta deve ser excluida')
def validar_conta_excluida(context):
    context.react.conta.validar_exclusao_conta(context)