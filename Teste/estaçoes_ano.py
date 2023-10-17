# definir as estaçoes do ano
verao = (12, 1, 2)
outono = (3, 4, 5)
inverno = (6, 7, 8)
primavera = (9, 10, 11)

dia = int(input("Digite o dia:\n"))
mes = int(input("Digite o mês:\n"))
ano = int(input("Digite o ano:\n"))

# validação dos dados

if dia < 1 or dia > 31:
    print("Dia invalido")
elif mes < 1 or mes > 12:
    print("Mes invalido")
elif ano < 0:
    print("Ano invalido")

# determinaçoes para as estaçoes

if mes in verao:
    estaçao = "Verao"
elif mes in outono:
    estaçao = "Outono"
elif mes in inverno:
    estaçao = "Inverno"

else:
    estaçao = primavera

print(f"A estação é {estaçao} do mês {mes} e do ano {ano}.")