import json

# model responsável por controlar o banco de dados, nesse caso o json.

class Arquivo:
    """
    Classe Arquivo com atributo nome.
    """
    def __init__(self,nome):
        # Metodo construtor
        self.nome = nome
        
    def abrir_arquivo(self):
        """
        Abre o arquivo de acordo com o nome passado na instância.
        CUIDADO! o nome deve ser exatamente igual ao nome do json, sujeito a quebra do código completo.
        """
        with open(self.nome,'r',encoding='utf-8') as arq:
            return json.load(arq)
            
    def escrever_arq(self,novo):
        """
        Refaz todo o arquivo json com um novo dicionário, com a formatação correta.
        """
        with open(self.nome,'w',encoding='utf-8') as arq:
            json.dump(novo,arq,indent=4)





