def salario_liquido(valor_hora,hora_trabalhada):
    salarioBruto= valor_hora * hora_trabalhada
    imposto_de_renda = salarioBruto*0.11
    desconto_inss = salarioBruto*0.09
    desconto_sindicato = salarioBruto*0.04
    salario_liquido = salarioBruto-(imposto_de_renda+desconto_inss+desconto_sindicato)
    print(f"+Salário Bruto: R${salarioBruto}")
    print(f"-IR(11%): R$ {imposto_de_renda}")
    print(f"-INSS(9%): R$ {desconto_inss}")
    print(f"-Sindicato(4%): R$ {desconto_sindicato}")
    print(f"=Salário Líquido: R$ {salario_liquido}")


valor_hora = float(input("Digite seu valor hora: "))
total_horas=float(input("Digite seu total horas trabalhadas: "))
salario_liquido(valor_hora,total_horas)


