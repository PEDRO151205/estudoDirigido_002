nome = input("Nome: ")
idade = int(input("Idade: "))

if idade >= 18:
 print(f"{nome}, você pode entrar.")
else:
 print(f"{nome}, você não pode entrar.")

def pode_entrar(idade):
    if idade >= 18:
        return True
    else:
        return False
    
def pode_entrar(idade):
    return idade >= 18

while True:
    entrada = input("Digite sua idade (ou 'sair' para encerrar): ").strip().lower()
    
    if entrada == "sair":
        print("Encerrando...")
        break
    
    if entrada.isdigit():
        idade = int(entrada)
        if pode_entrar(idade):
            print("Você pode entrar!")
        else:
            print("Você NÃO pode entrar!")
    else:
        print("Por favor, digite um número válido ou 'sair'.")    

forma = input("Forma de pagamento: ").lower()
valor = float(input("Valor: "))
if forma == "cartao" and valor > 20:
 print("Aceito!")
elif forma == "pix":
 print("Aceito!")
elif forma == "dinheiro" and valor == 10:
 print("Aceito!")
else:
 print("Não aceito.")

 def verifica_pagamento(forma, valor):
    if forma.lower() == "cartao" and valor >= 10:
        return "Pagamento aprovado no cartão."
    elif forma.lower() == "dinheiro" and valor >= 5:
        return "Pagamento aprovado em dinheiro."
    else:
        return "Pagamento recusado."

while True:
    entrada = input("Digite a forma de pagamento (cartao/dinheiro) ou 'sair' para encerrar: ").strip().lower()
    
    if entrada == "sair":
        print("Encerrando...")
        break
    
    valor_str = input("Digite o valor: ")
    
    if valor_str.replace('.', '', 1).isdigit():
        valor = float(valor_str)
        resultado = verifica_pagamento(entrada, valor)
        print(resultado)
    else:
        print("Valor inválido! Digite um número.")   
    
def verifica_pagamento(forma, valor):
    if forma == "cartao" and valor >= 10:
        return "Pagamento aprovado no cartão."
    elif forma == "dinheiro" and valor >= 5:
        return "Pagamento aprovado em dinheiro."
    else:
        return "Pagamento recusado."

for i in range(3):
    print(f"\nPedido {i+1}:")
    
    forma = input("Digite a forma de pagamento (cartao/dinheiro): ").strip().lower()
    valor_str = input("Digite o valor: ")
    
    if valor_str.replace('.', '', 1).isdigit():
        valor = float(valor_str)
        resultado = verifica_pagamento(forma, valor)
        print(resultado)
    else:
        print("Valor inválido! Digite um número.")    

    