def tornar_maiusculo(informacao = 'Sem parametros'):
    # .upper torna string maiuscula
    return informacao.upper()


def tornar_minusculo(informacao = "Sem parametros"):
    # .lower torna string minusculo
    return informacao.lower()


def printar_mensagem(mensagem, alteracao):
    mensagem_final = alteracao(mensagem)
    print(mensagem_final)

printar_mensagem("ja passa do meio dia", tornar_maiusculo)
