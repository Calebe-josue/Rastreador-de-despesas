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


def visualizar_despesas():
    arquivo = arq.abrir_arquivo()
    if not arquivo:
        return False
    else:
        for i in arquivo:
            print(f"{i["id"]} - {i["despesa"]} = R${i["valor"]} ")
        return True
                        

def remover_despesa(id):
    arquivo = arq.abrir_arquivo()
    if id>len(arquivo) or id<1:
        return False
    else:
        arquivo.pop(id-1)
        for i,v in enumerate(arquivo,start=1):
            v["id"]=i

        arq.escrever_arq(arquivo)
        return True

