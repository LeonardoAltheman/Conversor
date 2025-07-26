while True:
  print("Digite 1 para saber a temperatura em Celsius")
  print("Digite 2 para saber a temperatura em Fahrenheit")
  print("Digite 3 para saber o peso em KG")
  print("Digite 4 para saber o peso em libras")
  print("Digite 5 para saber a distância em KM")
  print("Digite 6 para saber a distância em milhas")
  print("Digite 7 para saber as horas em minutos")
  print("Digite 8 para saber os minutos em horas")
  print("Digite 0 para sair")

  opcao = input("Digite aqui sua opção: ")

  if opcao == "1":
    Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (Fahrenheit - 32) * 5 / 9
    print("A temperatura em Celsius é:", round(celsius, 1))

  elif opcao == "2":
    celsius = float(input("Digite a temperatura em Celsius: "))
    Fahrenheit = celsius * 9 / 5 + 32
    print("A temperatura em Fahrenheit é:", round(Fahrenheit, 1))

  elif opcao == "3":
    libras = float(input("Digite o peso em libras: "))
    kg = libras / 2.20462
    print("O peso em KG é:", round(kg, 1))

  elif opcao == "4":
    kg = float(input("Digite o peso em KG: "))
    libras = kg * 2.20462
    print("O peso em libras é:", round(libras, 1))

  elif opcao == "5":
    milhas = float(input("Digite a distância em milhas: "))
    km = milhas * 1.60934
    print("A distância em KM é:", round(km, 1))

  elif opcao == "6":
    km = float(input("Digite a distância em KM: "))
    milhas = km / 1.60934
    print("A distância em milhas é:", round(milhas, 1))

  elif opcao == "7":
    horas = float(input("Digite o número de horas: "))
    minutos = horas * 60
    print(f"{horas} horas equivalem a {round(minutos, 1)} minutos")

  elif opcao == "8":
    minutos = float(input("Digite o número de minutos: "))
    horas = minutos / 60
    print(f"{minutos} minutos equivalem a {round(horas, 1)} horas")

  elif opcao == "0":
    print("Obrigado por usar o nosso programa! Até mais")
    break

  else:
    print("Erro: opção inválida. Tente novamente.")