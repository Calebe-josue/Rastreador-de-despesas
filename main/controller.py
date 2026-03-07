import model

# Controlador responsável por interagir com o view e model

arq = model.Arquivo('despesas.json')

def pegar_id(arq) -> int:
    """Pega o id do último item do json. Se o json estiver vazio, começa no id 1"""
    if not arq:
        return 1
    
    maior = 0
    for i in arq:
        if i["id"]>maior:
            maior = i["id"]

    return maior+1


def adicionar_despesa(descricao,valor):
    """
    Adiciona despesa no json com formato e campos corretos.
    """
    arquivo = arq.abrir_arquivo()
    id = pegar_id(arquivo)
    arquivo.append({
        "id": id,
        "despesa": descricao,
        "valor":valor
    })
    arq.escrever_arq(arquivo)


def visualizar_despesas() -> bool:
    """
    Visualiza todas as despesas presentes no json. Retorna valor booleano
    """
    arquivo = arq.abrir_arquivo()
    if not arquivo:
        print('Sem despesas cadastradas!')
    else:
        for i in arquivo:
            print(f"{i["id"]} - {i["despesa"]} = R${i["valor"]} ")
        return True
                        

def remover_despesa(id) -> bool:
    """
    Remove uma despesa pelo id que contem no json. Refatora todo o ID de todos os itens do json após remover 1 item
    """
    arquivo = arq.abrir_arquivo()
    if id>len(arquivo) or id<1:
        return False
    else:
        arquivo.pop(id-1)
        for i,v in enumerate(arquivo,start=1):
            v["id"]=i

        arq.escrever_arq(arquivo)
        return True
    

def resumo_todas_despesas() -> float:
    """
    Pega o campo "valor" do json de todos os itens e soma.
    """
    arquivo = arq.abrir_arquivo()
    if not arquivo:
        print('Sem despesas cadastradas!')
    resumo_valor = 0
    for i in arquivo:
        resumo_valor += i["valor"]
    return resumo_valor


def editar_despesa(id,despesa="Sem informação",valor=0) -> None:
    """
    Edita algum item do json pelo id
    """
    arquivo = arq.abrir_arquivo()
    for i in arquivo:
        if i["id"]==id:
            i["despesa"]=despesa
            i["valor"]=valor
    arq.escrever_arq(arquivo) 
        