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