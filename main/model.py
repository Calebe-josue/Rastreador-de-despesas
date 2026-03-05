import json


class Arquivo:
    def __init__(self,nome):
        self.nome = nome
        
    def abrir_arquivo(self):
        with open(self.nome,'r',encoding='utf-8') as arq:
            return json.load(arq)
            
    def escrever_arq(self,novo):
        with open(self.nome,'w',encoding='utf-8') as arq:
            json.dump(novo,arq,indent=4)




