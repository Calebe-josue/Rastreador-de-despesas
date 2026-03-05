import json

nome = "despesas.json"

def abrir_arquivo():
    with open(nome,'r',encoding='utf-8') as arq:
        return json.load(arq)
        
def escrever_arq(novo):
    with open(nome,'w',encoding='utf-8') as arq:
        json.dump(novo,arq,indent=4)


