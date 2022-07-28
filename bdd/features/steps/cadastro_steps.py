from behave import given, when , then
import time

@given(u'que acesse o formulario de cadastro')
def acessar_pagina_cadastro(context):
    context.react.home.acessar_registro(context)


@when(u'preencher as informações necessárias')
def step_impl(context):
    raise NotImplementedError(u'STEP: When preencher as informações necessárias')


@then(u'o usuario deve ser cadastrado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o usuario deve ser cadastrado')