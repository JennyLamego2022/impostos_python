import json
import sys

for line in sys.stdin:
    if line.strip() == '':
        break
    operations = json.loads(line)

    quantidade_acoes_atual = 0
    media_ponderada_atual = 0.0

    prejuizo_passado = 0.0
    impostos = []

    for operation in operations:
        if operation['operation'] == 'buy':
            quantidade_acoes_compradas = operation['quantity']
            valor_compra = float(format(operation['unit-cost'], '2f'))
            quantidade_acoes_atual += quantidade_acoes_compradas
            media_ponderada_atual = round(((quantidade_acoes_atual - quantidade_acoes_compradas) * media_ponderada_atual +
                                           quantidade_acoes_compradas * valor_compra) / quantidade_acoes_atual, 2)
            impostos.append({'tax': '{:.2f}'.format(0)})
        else:
            quantidade_acoes_vendidas = operation['quantity']
            valor_venda = float(format(operation['unit-cost'], '2f'))
            if quantidade_acoes_vendidas > quantidade_acoes_atual:
                raise ValueError('Operação inválida')
            valor_total_venda = quantidade_acoes_vendidas * valor_venda
            valor_total_compra = quantidade_acoes_vendidas * media_ponderada_atual
            lucro = float(format(valor_total_venda -
                          valor_total_compra - prejuizo_passado, '2f'))
            if lucro <= 0:
                impostos.append({'tax': '{:.2f}'.format(0)})
                prejuizo_passado = abs(lucro)
            else:
                if valor_total_venda <= 20000:
                    impostos.append({'tax': '{:.2f}'.format(0)})
                    prejuizo_passado += lucro
                else:
                    imposto = round(lucro * 0.2, 2)
                    impostos.append(
                        {'tax': '{:.2f}'.format(round(imposto, 2))})
                    prejuizo_passado = 0.0
            quantidade_acoes_atual -= quantidade_acoes_vendidas

    # print(json.dumps(impostos))
    sys.stdout.write(json.dumps(impostos) + "\n")
    sys.stdout.flush()
