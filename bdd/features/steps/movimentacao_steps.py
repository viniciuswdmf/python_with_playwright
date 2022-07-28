from behave import given, when, then 

@given(u'que tenha acessado a pagina de movimentacoes')
def acessar_pagina_movimentacoes(context):
    context.react.home.acessar_movimentacao(context)


@when(u'preencher os dados necessarios')
def preencher_movimentacao(context):
    context.react.movimentacao.cadastrar_movimentacao(context, "teste_qa", "35", "Ibrahimovic", '797857')


@then(u'a movimentacao deve ser cadastrada')
def validar_movimentacao(context):
    context.react.movimentacao.validar_cadastro_movimentacao(context)

####################alterar movimentacao
@given(u'que tenha acessado a pagina de extrato')
def acessar_pagina_extrato(context):
    context.react.home.acessar_extrato(context)


@given(u'selecionado uma movimentacao')
def acessar_primeira_movimentacao(context):
    context.react.extrato.selecionar_primeira_movimentacao(context)


@when(u'preencher os dados a serem alterados')
def preencher_dados_alteracao(context):
    context.react.movimentacao.alterar_movimentacao(context, "lalalala", "22", "Eto'o", '797854')


@then(u'a movimentação deve ser alterada')
def validar_alteracao(context):
    context.react.movimentacao.validar_cadastro_movimentacao(context)

    ################excluir movimentacao

@when(u'excluir uma movimentacao')
def excluir_movimentacao(context):
    context.react.extrato.excluir_primeira_movimentacao(context)


@then(u'a mesma deve ser removida com sucesso')
def validar_exclusao(context):
    context.react.extrato.validar_exclusao_primeiro_item(context)