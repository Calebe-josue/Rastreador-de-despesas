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
            try:
                estado = controller.visualizar_despesas()
                if estado==True:
                    op = int(input('Digite o id da despesa que deseja remover\n'))
                else:
                    
            except (KeyboardInterrupt,ValueError,IndexError):
                print('Erro, id inválido')
            else:
                print(controller.remover_despesa(op))
        elif op==4:
            controller.visualizar_despesas()
    
        elif op==5:
            pass            