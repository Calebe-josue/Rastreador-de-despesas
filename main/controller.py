import model

arq = model.Arquivo('despesas.json')
def pegar_id(arq):
    if not arq:
        return 1
    
    maior = 0
    for i in arq:
        if i["id"]>maior:
            maior = i["id"]

    return maior+1


def adicionar_despesa(descricao,valor):
    arquivo = arq.abrir_arquivo()
    id = pegar_id(arquivo)
    arquivo.append({
        "id": id,
        "despesa": descricao,
        "valor":valor
    })
    arq.escrever_arq(arquivo)


