#language:pt

Funcionalidade: Cadastrar uma nova conta

Contexto: Estar logado
    Dado que esteja logado

# @cadastrar_conta
# Cenário: Cadastrar uma conta
#     Dado que tenha acessado a pagina de conta
#     Quando preencher o nome da conta
#     Então a conta deve ser cadastrada

@excluir_primeira_conta
Cenário: Excluir a primeira conta
    Dado que tenha acessado a pagina de conta
    Quando clicar em excluir a primeira conta
    Então a conta deve ser excluida