print("Cadastro de Clientes")
print("0 - Fim")
print("1 - Inclui")
print("2 - Altera")
print("3 - Exclui")
print("4 - Consulta")

opcao = int(input("Digite a opção desejada: "))

if opcao == 0:
  print("Fim")
elif opcao == 1:
  print("Inclui")
elif opcao == 2:
  print("Altera")
elif opcao == 3:
  print("Exclui")
elif opcao == 4:
  print("Consulta")
else:
  print("Item não encontrado")