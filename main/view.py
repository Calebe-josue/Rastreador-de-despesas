import controller

menu = ["Adicionar despesa","Atualizar despesa","Excluir despesa","Visualizar todas as despesas","Resumo de todas as despesas",]

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
            descricao = str(input('Digite a despesa\n'))
            valor = float(input('Digite o valor da despesa\n'))
            controller.adicionar_despesa(descricao,valor)

        elif op==2:
            pass

        elif op==3:
            pass
        
        elif op==4:
            arquivo = controller.visualizar_despesas()
            for i in arquivo:
                for c,v in i.items():
                    print(f"{c} - {v}")
                    