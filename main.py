"""
Nome: Rafael Oliveira Tavares Pinto
Curso: Análise e Desenvolvimento de Sistemas
"""
import json

def mostrar_menu_pricipal():
    # Mostrar o menu principal
    print("||||| MENU PRINCIPAL |||||")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(9) Sair.")


def selecionar_menu_principal(menu_principal):
    if menu_principal == "1":
        print("\n- MENU DE OPERAÇÕES [ESTUDANTES] -")
        mostrar_menu_operacoes()
        return "estudantes"
    elif menu_principal == "2":
        print("\n- MENU DE OPERAÇÕES [PROFESSORES] -")
        mostrar_menu_operacoes()
        return "professores"
    elif menu_principal == "3":
        print("\n- MENU DE OPERAÇÕES [DISCIPLINAS] -")
        mostrar_menu_operacoes()
        return "disciplinas"
    elif menu_principal == "4":
        print("\n- MENU DE OPERAÇÕES [TURMAS] -")
        mostrar_menu_operacoes()
        return "turmas"
    elif menu_principal == "5":
        print("\n- MENU DE OPERAÇÕES [MATRÍCULAS] -")
        mostrar_menu_operacoes()
        return "matriculas"

def mostrar_menu_operacoes():
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(9) Voltar ao menu principal.")

def acessar_menu_operacoes(menu_operacoes, nome_arquivo):
    if menu_operacoes == "1":
        # Coletar o cadastro a ser adicionado e incluí-lo em uma lista
        incluir(nome_arquivo)
    elif menu_operacoes == "2":
        # Listar os cadastros inclusos na lista
        listar(nome_arquivo)
    elif menu_operacoes == "3":
        # Atualizar os cadastros inclusos na lista
        atualizar(nome_arquivo)
    elif menu_operacoes == "4":
        # Excluir os cadastros inclusos na lista
        excluir(nome_arquivo)
    elif menu_operacoes == "9":
        print("")
        return False
    return True
def incluir(nome_arquivo):
    cadastros = ler_dados(nome_arquivo)
    print("\n===== INCLUSÃO =====\n")
    if nome_arquivo == "estudantes" or nome_arquivo == "professores":
        codigo = chamar_excecao_codigo()
        nome = input("Informe o nome: ")
        cpf = input("Informe o CPF: ")
        cadastros.append({"codigo": codigo, "nome": nome, "cpf": cpf})
    elif nome_arquivo == "disciplinas":
        codigo_disciplina = chamar_excecao_codigo("Informe o código da disciplina: ")
        nome_disciplina = input("Informe o nome: ")
        cadastros.append({"codigo_disciplina": codigo_disciplina, "nome_disciplina": nome_disciplina})
    elif nome_arquivo == "turmas":
        codigo_turma = chamar_excecao_codigo("Informe o código da turma: ")
        for cadastrado in ler_dados(nome_arquivo):
            if codigo_turma == cadastrado['codigo_turma']:
                print("\nCódigo de turma já registrado. Escolha outro código.")
                return
        codigo_professor = chamar_excecao_codigo("Informe o código do professor: ")
        codigo_disciplina = chamar_excecao_codigo("Informe o código da disciplina: ")
        cadastros.append({"codigo_turma": codigo_turma, "codigo_professor": codigo_professor, "codigo_disciplina": codigo_disciplina})
    else:
        codigo_turma = chamar_excecao_codigo("Informe o código da turma: ")
        for cadastrado in ler_dados(nome_arquivo):
            if codigo_turma == cadastrado['codigo_turma']:
                print("\nCódigo de turma já registrado. Escolha outro código.")
                return
        codigo_estudante = chamar_excecao_codigo("Informe o código do estudante: ")
        cadastros.append({"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante})

    adicionar_dados(nome_arquivo, cadastros)
    input("Pressione ENTER para continuar.")

def listar(nome_arquivo):
    print("\n===== LISTAMENTO =====\n")
    if ler_dados(nome_arquivo) == []:
        print("Não há cadastros.")
        input("Pressione ENTER para continuar.")
    else:
        for cadastrado in ler_dados(nome_arquivo):
            if nome_arquivo == "estudantes" or nome_arquivo == "professores":
                print(f"- Código: {cadastrado['codigo']}, Nome: {cadastrado['nome']}, CPF: {cadastrado['cpf']}")
            elif nome_arquivo == "disciplinas":
                print(f"- Código: {cadastrado['codigo_disciplina']}, Nome: {cadastrado['nome_disciplina']}")
            elif nome_arquivo == "turmas":
                print(f"- Código Turma: {cadastrado['codigo_turma']}, Código Professor: {cadastrado['codigo_professor']}, Código Disciplina: {cadastrado['codigo_disciplina']}")
            else:
                print(f"- Código Turma: {cadastrado['codigo_turma']}, Código Estudante: {cadastrado['codigo_estudante']}")
        input("Pressione ENTER para continuar.")

def atualizar(nome_arquivo):
    print("\n===== ATUALIZAÇÃO =====\n")
    cadastros = ler_dados(nome_arquivo)
    if cadastros == []:
        print("Não há cadastros.")
        input("Pressione ENTER para continuar.")
    else:
        codigo = chamar_excecao_codigo("Informe o código a ser atualizado: ")
        for cadastro in cadastros:
            if nome_arquivo == "estudantes" or nome_arquivo == "professores":
                if cadastro['codigo'] == codigo:
                    cadastro['codigo'] = chamar_excecao_codigo("Informe um novo código: ")
                    cadastro['nome'] = input("Informe um novo nome: ")
                    cadastro['cpf'] = input("Informe o CPF: ")
                    adicionar_dados(nome_arquivo, cadastros)
                    input("Pressione ENTER para continuar.")
            elif nome_arquivo == "disciplinas":
                if cadastro["codigo_disciplina"] == codigo:
                    cadastro['codigo_disciplina'] = chamar_excecao_codigo("Informe um novo código para a disciplina: ")
                    cadastro['nome_disciplina'] = input("Informe o nome: ")
                    adicionar_dados(nome_arquivo, cadastros)
                    input("Pressione ENTER para continuar.")
            elif nome_arquivo == "turmas":
                if cadastro["codigo_turma"] == codigo:
                    cadastro['codigo_turma'] = chamar_excecao_codigo("Informe um novo código para a turma: ")
                    cadastro['codigo_professor'] = chamar_excecao_codigo("Informe um novo código para o professor: ")
                    cadastro['codigo_disciplina'] = chamar_excecao_codigo("Informe um novo código para a disciplina: ")
                    adicionar_dados(nome_arquivo, cadastros)
                    input("Pressione ENTER para continuar.")
            else:
                if cadastro["codigo_turma"] == codigo:
                    cadastro['codigo_turma'] = chamar_excecao_codigo("Informe um novo código para a turma: ")
                    cadastro['codigo_estudante'] = chamar_excecao_codigo("Informe um novo código para o estudante: ")
                    adicionar_dados(nome_arquivo, cadastros)
                    input("Pressione ENTER para continuar.")

def excluir(nome_arquivo):
    cadastros = ler_dados(nome_arquivo)
    print("\n===== EXCLUSÃO =====\n")
    if cadastros == []:
        print("Não há cadastros.")
        input("Pressione ENTER para continuar.")
    else:
        codigo = chamar_excecao_codigo("Informe o código a ser excluído: ")
        for cadastro in cadastros:
           if nome_arquivo == "estudantes" or nome_arquivo == "professores":
               cod = "codigo"
           elif nome_arquivo == "disciplinas":
               cod = "codigo_disciplina"
           elif nome_arquivo == "turmas" or nome_arquivo == "matriculas":
               cod = "codigo_turma"

           if cadastro[cod] == codigo:
               cadastros.remove(cadastro)
               adicionar_dados(nome_arquivo, cadastros)
               input("Pressione ENTER para continuar.")

def adicionar_dados(nome_arquivo, data):
    with open(nome_arquivo + ".json", "w", encoding="utf-8") as arquivo:
        json.dump(data, arquivo)
        arquivo.close()

def ler_dados(nome_arquivo):
    try:
        with open(nome_arquivo + ".json", "r", encoding="utf-8") as arquivo:
            lista = json.load(arquivo)

        return lista
    except:
        return []

def chamar_excecao_codigo(input_string="Informe o código: "):
    while True:
        try:
            codigo = int(input(input_string))
            return codigo
        except ValueError:
            print("\nCódigo inválido. Digite um número.\n")
            continue

#Iniciar o algoritmo em um looping até o usuário decidir sair do programa
menu_principal_is_on = True
while menu_principal_is_on:
    # Mostrar o menu principal
    mostrar_menu_pricipal()
    # Coletar a opção desejada do menu principal
    menu_principal = input("Informe a opção desejada: ")
    # Verificar se a opção escolhida do menu principal é válida
    if menu_principal not in "123459" or menu_principal == "":
        print("\nOpção inválida. Por favor, insira uma opção válida.\n")
        continue
    elif menu_principal == "9":
        break

    menu_operacoes_is_on = True
    while menu_operacoes_is_on:
        # Mostrar o menu de operações
        nome_arquivo = selecionar_menu_principal(menu_principal)
        # Coletar a opção desejada do menu de operações
        menu_operacoes = input("Informe a opção desejada: ")
        # Verificar se a opção escolhida do menu de operações é válida
        if menu_operacoes not in "12349" or menu_operacoes == "":
            print("\nOpção inválida. Por favor, insira uma opção válida.\n")
            continue
        # Executar os comandos de cada uma das opções do menu de operações
        menu_operacoes_is_on = acessar_menu_operacoes(menu_operacoes, nome_arquivo)

print("Finalizando aplicação...")
