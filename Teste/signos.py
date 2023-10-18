# lista dos signos

signos = [("Áries",(21, 3),(20, 4)),
        ("Touro", (21,4), (20,5)),
        ("Gêmeos",(21,5), (20,6)),
        ("Câncer", (21,6),(22,7)),
        ("Leão",(23,7),(22,8)),
          ("Virgem",(23,8),(22,9)),
        ("Libra",(23,9),(22,10)),
        ("Escorpião",(23,10),(21,11)),
        ("Sagitario",(22,11),(21,12)),
        ("Capricórnio",(22,12),(20,1)),
        ("Aquario",(21,1),(18,2)),
        ("Peixes",(19,2),(20,3))]

aniversario = input("Digite o seu aniversário no formato dd/mm:\n")

aniversario = list(map(int,aniversario.split("/")))

signo_us = None

for signo in signos:
    nome, inicio, fim = signo

    dia_inicio, mes_inicio = inicio
    dia_fim, mes_fim = fim

    dia_usuario, mes_usuario = aniversario

    if mes_usuario == mes_inicio or mes_usuario == mes_fim:
        if mes_usuario == mes_inicio and dia_usuario >= dia_inicio:
            signo_us = nome
            break
        elif mes_usuario == mes_fim and dia_usuario <= dia_fim:
            signo_us = nome
            break

if signo_us:
    print(f"O seu signo é {signo_us}")
else:
    print("Não foi possivel determinar o seu signo ")