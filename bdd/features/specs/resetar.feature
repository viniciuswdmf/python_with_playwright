#language: pt

Funcionalidade: Resetar site de testes
    Como um usuario
    Quero resetar as informaçoes do site
    Para utiliza-lo do zero novamente

Contexto:
    Dado que esteja logado

@resetar
Cenário: Resetar site
    Quando clicar no menu referente a opcao reset
    Então o site deve ser resetado
