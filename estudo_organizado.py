import json
import os

ARQUIVO = "tarefas_estudos.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\nTarefas de Estudo:")
    for i, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['descricao']} - {status}")
    print()

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a ser marcada como concluída: "))
        if 1 <= indice <= len(tarefas):
            tarefas[indice - 1]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida!")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a ser removida: "))
        if 1 <= indice <= len(tarefas):
            tarefa = tarefas.pop(indice - 1)
            salvar_tarefas(tarefas)
            print(f"Tarefa '{tarefa['descricao']}' removida com sucesso!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida!")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("""
========= Gerenciador de Estudos =========
1. Listar tarefas
2. Adicionar tarefa
3. Marcar tarefa como concluída
4. Remover tarefa
5. Sair
""")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo do programa. Bons estudos!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
