
contas = []

# Operação - 1: Criar conta
def criar_conta():
   verificador_conta_existe = False
   dados_nova_conta = {}
   dados_nova_conta["numero_conta"] = input("Digite o número da nova conta: \n>>> ")

   for conta_em_consulta in contas:
      if conta_em_consulta["numero_conta"] == dados_nova_conta["numero_conta"]:
       verificador_conta_existe = True
       break

   if verificador_conta_existe == True:
      print("\nO numero da conta já existe! Tente novamente.")
   else:
      dados_nova_conta["saldo_conta"] = float(input("Digite o saldo da nova conta:\n>>> R$"))
      contas.append(dados_nova_conta)
      print("\nOperação efetuada com sucesso!")

# Operação - 2: Remover Conta
def remover_conta():
  numero_conta = input("Digite o número da conta para remover:\n>>>")
  conta_encontrada = False
  for conta_em_consulta in contas:
      if conta_em_consulta["numero_conta"] == numero_conta:
        conta_encontrada = True
        contas.remove(conta_em_consulta)
        print("\nOperação efetuada com sucesso!")
        break
  if not conta_encontrada:
        print("\nConta inexistente. Tente novamente")

# Operação - 3: Listar contas
def listar_contas():
  if len(contas) == 0:
    print("\nNão há contas cadastradas neste banco.")
  else:
     index = 1
     for conta_em_consulta in contas:
       if conta_em_consulta["saldo_conta"] >= 0:
           status = "Positivo"
       else:
         status = "Negativo"
       print(f"{index} - Número da Conta: {conta_em_consulta['numero_conta']} | Saldo em conta: R$ {conta_em_consulta['saldo_conta']:.2f} ({status}) ")
       index += 1

# Operação - 4: Adicionar saldo
def add_saldo():
  numero_conta = input("Digite o número da sua conta:\n>>>")
  for conta_em_consulta in contas:
    if conta_em_consulta["numero_conta"] == numero_conta:
      valor_creditado = float(input("Digite o valor a ser creditado:\n>>> R$"))
      if valor_creditado < 0:
        print("Valores negativos não podem ser creditados! Tente novamente.")
        return
      else:
        conta_em_consulta["saldo_conta"] += valor_creditado
        print("O saldo foi adicionado a sua conta!")
        return
  print("\nConta não encontrada. Tente novamente.")

# Operação - 5: Remover saldo
def remover_saldo():
  numero_conta = input("Digite o número da sua conta:\n>>>")
  for conta_em_consulta in contas:
    if conta_em_consulta["numero_conta"] == numero_conta:
      valor_debitado = float(input("Digite o valor a ser debitado:\n>>> R$"))
      if valor_debitado < 0:
        print("Valores negativos não podem ser debitados! Tente novamente.")
        return
      else:
        conta_em_consulta["saldo_conta"] -= valor_debitado
        print("O saldo foi debitado da sua conta!")
        return
  print("\nConta não encontrada. Tente novamente.")

# Operação - 6: transferir saldo
def transfer_saldo():
  conta_p = input("Digite o número da sua conta: \n>>>")
  verificador_etapa = 0
  # Procura a primeira conta.
  for conta_em_consulta in contas:
    if conta_em_consulta["numero_conta"] == conta_p:
      verificador_etapa = 1
      conta_d = input("Digite o número da conta destino: \n>>>")
      # Verifica se a transferência é pra mesma conta.
      if conta_d != conta_p:
        # Procura a segunda conta.
        for conta_d_em_consulta in contas:
          if conta_d_em_consulta["numero_conta"] == conta_d:
            verificador_etapa = 3
            valor_transfer = float(input("Digite o valor a ser transferido: \n>>> R$ "))
            # Verifica se o valor é negativo.
            if valor_transfer < 0:
              print("\nNão é possível transferir valores negativos.")
              break
              # Verifica se o saldo é suficiente.
            elif valor_transfer > conta_em_consulta["saldo_conta"]:
              print("\nNão é possível transferir um valor maior que o seu saldo!")
              break
            else:
              conta_em_consulta["saldo_conta"] -= valor_transfer
              conta_d_em_consulta["saldo_conta"] += valor_transfer
              print("\nOperação efetuada com sucesso!")
              break

        print()
      else:
       verificador_etapa = 2
       break

  if verificador_etapa == 0:
   print("\nConta não encontrada. Tente novamente")
  elif verificador_etapa == 1:
   print("\nConta destino não foi encontrada. Tente novamente")
  elif verificador_etapa == 2:
    print("\nNão é possível transferir dinheiro para mesma conta!")

# Operação - 7: Consultar saldo em conta
def consultar_saldo():
  numero_conta = input("Digite o número da sua conta para consultar o saldo:\n>>> ")
  for conta_em_consulta in contas:
    if conta_em_consulta["saldo_conta"] >= 0:
      status = "Positivo"
    else:
      status = "Negativo"
    if conta_em_consulta["numero_conta"] == numero_conta:
      print(f'\nO saldo da conta é: R$ {conta_em_consulta["saldo_conta"]:.2f} ({ status })')
      return
  print("\nNúmero da conta não encontrada! Tente novamente")

# > Tela inicial do Sistema Bancário <
print(f">>>> Bem Vindo ao Sistema Bancário <<<<")
while True:
  print("\n### Menu ###")
  print("0 - Sair")
  print("1 - Criar uma nova conta")
  print("2 - Remover uma conta")
  print("3 - Listar todas as contas existentes")
  print("4 - Adicionar saldo na conta")
  print("5 - Remover saldo da conta")
  print("6 - Transferir valor para outra conta")
  print("7 - Consultar saldo")
  numero_operacao = input("Selecione a operação que deseja realizar: \n>>> ")

  if numero_operacao == "0":
    print("\nSistema Encerrado.")
    break

# Operação - 1
  elif numero_operacao == "1":
    criar_conta()

# Operação - 2
  elif numero_operacao == "2":
    remover_conta()

# Operação - 3
  elif numero_operacao == "3":
    listar_contas()

# Operação - 4
  elif numero_operacao == "4":
    add_saldo()

# Operação - 5
  elif numero_operacao == "5":
    remover_saldo()

# Operação - 6
  elif numero_operacao == "6":
    transfer_saldo()

# Operação - 7
  elif numero_operacao == "7":
    consultar_saldo()

# Operação Inválida
  else:
      print("\nOperação Inválida.")