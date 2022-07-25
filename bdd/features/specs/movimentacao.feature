#language:pt

Funcionalidade: Cadastrar Movimentações na ferramenta

Contexto: Estar logado
    Dado que esteja logado

Cenário: Cadastrar uma movimentação
    Dado que tenha acessado a pagina de movimentacoes
    Quando preencher os dados necessarios
    Então a movimentacao deve ser cadastrada