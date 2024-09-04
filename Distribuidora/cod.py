import json


def processar_faturamento(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        dados = json.load(file)

    faturamentos = [item['valor']
                    for item in dados['faturamento_diario'] if item['valor'] > 0]

    if not faturamentos:
        raise ValueError("Não há dados de faturamento para processar.")

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    media_mensal = sum(faturamentos) / len(faturamentos)

    dias_acima_da_media = len(
        [valor for valor in faturamentos if valor > media_mensal])

    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }


resultado = processar_faturamento('dados.json')

print(f"Menor faturamento: {resultado['menor_faturamento']}")
print(f"Maior faturamento: {resultado['maior_faturamento']}")
print(f"Número de dias com faturamento acima da média: {
      resultado['dias_acima_da_media']})")
