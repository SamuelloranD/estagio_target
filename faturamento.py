import json

with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

faturamento_validos = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_faturamento = min(faturamento_validos)

maior_faturamento = max(faturamento_validos)

media_faturamento = sum(faturamento_validos) / len(faturamento_validos)

dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_faturamento)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
