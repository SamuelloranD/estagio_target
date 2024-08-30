faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

valor_total = sum(faturamento.values())

percentual_sp = (faturamento["SP"] / valor_total) * 100
percentual_rj = (faturamento["RJ"] / valor_total) * 100
percentual_mg = (faturamento["MG"] / valor_total) * 100
percentual_es = (faturamento["ES"] / valor_total) * 100
percentual_outros = (faturamento["Outros"] / valor_total) * 100

print(f"Percentual de SP: {percentual_sp:.2f}%")
print(f"Percentual do RJ: {percentual_rj:.2f}%")
print(f"Percentual de MG: {percentual_mg:.2f}%")
print(f"Percentual do ES: {percentual_es:.2f}%")
print(f"Percentual de Outros: {percentual_outros:.2f}%")