#language: pt

@login
Funcionalidade: Login no Ecommerce Porto Seguro
    Como um usuário do Ecommerce
    Quero realizar login 
    Para realizar compras ou guardar produtos para comprar mais tarde no Ecommerce.

Cenário: Fazer login com sucesso
    Quando realizar login com CPF e senha válidos
    Então deve validar que o login foi realizado com sucesso