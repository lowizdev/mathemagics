valor_inicial = 0
percentual_rendimento = 0
rendimento_total = 0
qtd_parcelas = 0
valor_parcela = 0

for i in range(1, qtd_parcelas+1):
    parcela_rendimento = (valor_inicial * percentual_rendimento)
    rendimento_total += parcela_rendimento
    valor_inicial -= valor_parcela 
    valor_inicial += parcela_rendimento
    print(rendimento_total)
    print(valor_inicial)
    
print(5*"-")
print(rendimento_total)
print(valor_inicial)
