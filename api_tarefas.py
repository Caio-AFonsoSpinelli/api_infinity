todas_as_tarefas = {}

def criar_tarefas():

    tarefa = {}
    nome = input("Qual o Nome da tarefa: ")
    categoria = input("Qual a categoria da tarefa: ")
    prioridade = input("Qual a prioridade dessa tarefa (alta, média, baixa): ")
    descricao = input("Qual a sua descrição: ")

    tarefa["prioridade"] = prioridade
    tarefa["tarefa"] = nome
    tarefa["descricao"] = descricao
    tarefa["concluido"] = False

    if categoria not in todas_as_tarefas:
        todas_as_tarefas[categoria] = []

    todas_as_tarefas[categoria].append(tarefa)
    #todas_as_tarefas.append(tarefa) <- obs
    

def lista_de_tarefas():
    escolha = int(input("Como você deseja listar as tarefas?\n1 - Todas\n2 - Por Categoria\n3 - Por Prioridade\nEscolha: "))

    if escolha == 1: 
        for categoria, tarefa in todas_as_tarefas:
            print(f"Categoria: {categoria}")
            for tarefa in tarefa:
                print(f" - {tarefa}")

    elif escolha == 2: 
        categoria_escolhida = input("Qual categoria você deseja vizualizar: ")

        if categoria_escolhida in todas_as_tarefas:
            for tarefa in todas_as_tarefas[categoria_escolhida]:
                print(tarefa)
        else:
            print("Categoria não encontrada!") 

    elif escolha == 3: 
        prioridade_escolhida = input("Qual a prioridade que deseja visualizar (alta, média, baixa): ")
        for categoria, listas_tarefa in todas_as_tarefas.items():
            for tarefa in listas_tarefa: 
                if tarefa["prioridade"] == prioridade_escolhida: 
                    print(tarefa)
    else: 
        print("Opção invalida")

    

def tarefa_concluida():
    categoria_tarefa = input("Qual a categoria da tarefa que você deseja marcar como concluída: \n")
    nome_tarefa = input("Qual o nome da tarefa que você deseja marcar como concluída: \n")
    
    if categoria_tarefa in todas_as_tarefas:
        tarefas = todas_as_tarefas[categoria_tarefa]
        for tarefa in tarefas:
            if tarefa["tarefa"] == nome_tarefa:
                tarefa_c = int(input("1 - para tarefa concluída\n2 - para não concluída: "))
                if tarefa_c == 1:
                    tarefa["concluido"] = True
                else:
                    tarefa["concluido"] = False
                print("Tarefa alterada com sucesso!")
                return
        print("Tarefa não encontrada na categoria especificada, tente novamente!")
    else:
        print("Categoria não encontrada, tente novamente!")

def editar_tarefa():
    nome_atual = input("Qual o nome da tarefa que deseja editar: ")
    for tarefa in todas_as_tarefas:
        if tarefa["tarefa"] == nome_atual:
            novo_nome = input("Qual o novo nome da tarefa: ")
            nova_descricao = input("Qual a nova descrição da tarefa: ")

            # Atualizando o valor da chave "tarefa"
            tarefa["tarefa"] = novo_nome

            # Atualizando o valor da chave "descrição"
            tarefa["descricao"] = nova_descricao
            
            print("Tarefa editada com sucesso!")
            return
    print("Tarefa não encontrada.")


def remover_tarefa(): 
    remover = int(input("Qual tarefa vc quer remover: "))
    todas_as_tarefas.pop(remover)

    
print("Bem vindo ao tarefas CaioTesk")
while True: 
    print("O que Desja fazer agora com o CaioTesk? ")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marca como concluído")
    print("4 - Editar Tarefa")
    print("5 - Excluir Tarefa")
    op = int(input("Qual ação deseja: "))
    if op == 1: 
        criar_tarefas()
    elif op == 2:
        lista_de_tarefas()
    elif op == 3:
        tarefa_concluida()
    elif op == 4: 
        editar_tarefa()
    elif op == 5: 
        remover_tarefa()
    else:
        print("Erro tente novamente: ")
