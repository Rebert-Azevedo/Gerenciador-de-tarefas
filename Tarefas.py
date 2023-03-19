tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite sua nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def remover_tarefa():
    if len(tarefas) == 0:
        print("Não há nenhuma tarefa a ser removida.")
    else:
        print("Tarefas disponíveis:")
        for i in range(len(tarefas)):
            print(f"{i + 1}. {tarefas[i]}")
        escolha = int(input("Digite o número da tarefa que deseja remover: "))
        if escolha < 1 or escolha > len(tarefas):
            print("Escolha inválida.")
        else:
            tarefas.pop(escolha - 1)
            print("Tarefa removida com sucesso!")
            
def remover_todas_as_tarefas():
    if len(tarefas) == 0:
        print("Não há nenhuma tarefa para remover.")
    else:
        print("Tarefas disponíveis:")
    for i in range(len(tarefas)):
        print(f"{i}. {tarefas[i]}")
    tarefas.clear()
    print("Tarefas removidas com sucesso!")


def listar_tarefas():
    if len(tarefas) == 0:
        print("Não há tarefas a serem exibidas.")
    else:
        print("Tarefas disponíveis:")
        for i in range(len(tarefas)):
            print(f"{i + 1}. {tarefas[i]}")

while True:
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Incluir tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("4. Limpar lista de tarefas")
    print("0. Sair")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        adicionar_tarefa()
    elif escolha == 2:
        remover_tarefa()
    elif escolha == 3:
        listar_tarefas()
    elif escolha == 4:
        remover_todas_as_tarefas()
    elif escolha == 0:
        print("Saindo do programa...")
        break
    else:
        print("Escolha inválida. Tente novamente.")
        