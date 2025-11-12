# Desafio com 'Sets'

# Criar um programa que gere 3 listas de acordo com o que se pede:

# Lista 1 -> Funcionários que possuem carro e trabalham durante a noite.
# Lista 2 -> Funcionários que possuem carro e trabalham durante o dia.
# Lista 3 -> Funcionários que não possuem carro.


funcionarios = ["Maria", "Rozane", "Regina", "Lucio", "Rian", "Caio", "Gael"]
turno_dia = ["Maria", "Rozane", "Regina", "Gael"]
turno_noite = ["Lucio", "Rian", "Caio"]
tem_carro = ["Rozane", "Regina", "Caio", "Rian"]

func = set(funcionarios)
t_dia = set(turno_dia)
t_noite = set(turno_noite)
t_carro = set(tem_carro)


if __name__ == "__main__":

    print(
        f"Os funcionários que possuem carro e trabalham durante a noite são: {func & t_noite & t_carro}"
    )

    print(
        f"Os funcionários que possuem carro e trabalham durante o dia são: {func & t_dia & t_carro}"
    )

    print(f"Os funcionários que não possuem carro são: {func - t_carro}")
