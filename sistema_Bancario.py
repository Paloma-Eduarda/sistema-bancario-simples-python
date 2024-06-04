menu = """
============= MENU ============
      1 - SACAR
      2 - EXTRATO
      3 - DEPOSITAR
      0 - SAIR
===============================
      
      """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMETE_SAQUES = 3

while True:

    opcao =  int(input(menu))
    
    if opcao == 1:
       
        if saldo > 0 and numero_saques >= LIMETE_SAQUES:
            saque = float(input("Por favor, Informe o valor a ser sacado")) 
            
            if saque<=500 and saque<=saldo:
                saldo -= saque 
                numero_saques += 1
                extrato += f"Saque: R$ {saque:.2f}\n"
                print(f"seu novo saldo é {saldo}")

            else:
                print("O valor maximo de saque é de 500 reais")  
        else:
            
            print("Não será possivel realizar o saque, saldo insuficiente ou limite de saques excedido!")    
    elif opcao == 2:
        if extrato == "":
            print("Não foram realizadas movimentações")
        
        else:
            print(extrato)
            print(f"seu novo saldo é {saldo}, seu numero de saques hoje foi de {numero_saques}")    
        #print("Extrato")

    elif opcao == 3:
        
        deposito = float(input("Por favor, Informe o valor do deposito."))
        
        if deposito > 0:                 
            saldo += deposito 
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"seu novo saldo é {saldo}")

        else:
            print("Valor de deposito invalido")
            
    elif opcao == 0:
        print("Obrigada por usar nosso Sistema!")
        break
