while True:

#valores
    print("1.Criar")
    print("2.Atualizar")
    print("3.Eliminar")
    print("4.Sair")

    opcao = input("Selecione a opção desejada (1-4): ")

#operação
    if opcao == "1":
        print("Opção selecionada Criar")

    elif opcao == "2":
        print("Opção selecionada Atualizar")

    elif opcao == "3":
        print("Opção selecionada Eliminar")

    elif opcao == "4":
        print("Opção selecionada Sair. Programa finalizado")
        break
    else:
        print("Opção inválida")
