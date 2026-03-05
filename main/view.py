import controller

menu = ["Adicionar despesa","Atualizar despesa","Excluir despesa","Visualizar todas as despesas","Resumo de todas as despesas","Visualizar resumo das despesas de um mês específico"]

for i,v in enumerate(menu,start=1):
    print(f'{i} - {v}')


try:
    op = int(input('Escolha sua opção\n'))
except:
    print('Erro, escolha uma opção correta')
else:
    if op>len(menu) or op<1:
        print('opção inválida')
    else:
        if op==1:
            descricao = str(input('Digite a despesa'))
            valor = float(input('Digite o valor da despesa'))
            controller.adicionar_despesa(descricao,valor)
            