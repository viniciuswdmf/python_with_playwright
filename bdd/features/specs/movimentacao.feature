#language:pt

Funcionalidade: Cadastrar Movimentações na ferramenta

Contexto: Estar logado
    Dado que esteja logado

@cadastrar_movimentacao
Cenário: Cadastrar uma movimentação
    Dado que tenha acessado a pagina de movimentacoes
    Quando preencher os dados necessarios
    Então a movimentacao deve ser cadastrada

@alterar_movimentacao
Cenário: Alterar uma movimentação
    Dado que tenha acessado a pagina de extrato
    E selecionado uma movimentacao
    Quando preencher os dados a serem alterados
    Então a movimentação deve ser alterada

@excluir_movimentacao
Cenário: Excluir uma movimentação
    Dado que tenha acessado a pagina de extrato
    Quando excluir uma movimentacao
    Então a mesma deve ser removida com sucesso