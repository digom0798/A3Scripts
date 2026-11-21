#Valores
print("1.Criar")
print("2.Atualizar")
print("3.Eliminar")
print("4.Sair")

Opcao_menu = input("Escolha a opção do menu (1, 2, 3, 4): ")

#Operação
if Opcao_menu == '1':
    print ("Criar")

elif Opcao_menu == '2':
    print ("Atualizar")

elif Opcao_menu == '3':
    print ("Eliminar")

elif Opcao_menu == '4':
    pass
#nada acontece no 4 ou print ("")

else:
    print ("Opção inválida!")
