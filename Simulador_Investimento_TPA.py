while True:
    print("***********************************")
    print("     Seja bem-vindo(a) ao MyBank   ")
    print("      SIMULADOR DE INVESTIMENTO    ")
    print("***********************************")

    print ("Titulos disponiveis:")
    print ("1 - Tesouro Prefixado 2025")
    print ("2 - Tesouro Prefixado 2028")
    cliente = str(input("Qual titulo você gostaria de fazer uma simulação?:"))
    if cliente == '1':
        investir = float(input("Qual o valor você quer investir?:"))
        mês = float(input("Se você for investir todo o mês, qual o valor?:"))
        aportes = 32
        total = (mês * aportes) + investir
        rentabilidade = total / investir - 1 
        bruto = total * (rentabilidade/100)
        valorbruto = bruto + total
        IR = (15/100)
        b3 = (0.25/100) * 3
    else:
        investir = float(input("Qual o valor você quer investir?:"))
        mês = float(input("Se você for investir todo o mês, qual o valor?:"))
        aportes = 50
        tudo = (mês * aportes) + investir
        rentabilidade = total / investir - 1 
        bruto = total * (rentabilidade/100)
        valorbruto = bruto + total
        IR = (15/100)
        b3 = (0.25/100) * 5

    IRtudo = (valorbruto - total) * IR

    b3tudo = (valorbruto - total) * b3

    valorliquido = valorbruto - (IRtudo + b3tudo)

    print("***********************************")       
    print("      RESULTADO DA SIMULAÇÃO       ")
    print("***********************************")

    print("Valor inicial investido: {}".format(investir))
    print("Aportes de {} por {} meses".format(mês,aportes))
    print("Valor total investido {}".format(total))
    print("***********************************")  
    print("Valor Bruto: {}".format(valorbruto))
    print("I.R: {}".format(IRtudo))
    print("Taxa da B3: {}".format(b3tudo))
    print("Valor Liquido: {}".format(valorliquido))
    print("***********************************") 
    opcao = str(input("Deseja realizar outra simulação? s/n: "))
    if opcao == 'n':
        break
print ("Progrma Encerrado")



