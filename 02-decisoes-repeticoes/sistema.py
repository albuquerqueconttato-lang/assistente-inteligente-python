print("Sistema de Validação de Acesso")

while True:

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print(f"{nome}, acesso permitido.")

    elif idade >= 16:
        print(f"{nome}, acesso permitido com restrições.")

    else:
        print(f"{nome}, acesso negado.")

    continuar = input("Deseja realizar uma nova verificação? (s/n): ")

    if continuar.lower() != "s":
        print("Sistema encerrado.")
        break
