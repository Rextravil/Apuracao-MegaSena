import csv
import random

with open("resultados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    for i in range(10):
        identificador = "AP-" + "".join(
            random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6)
        )

        quantidade = random.randint(6, 15)
        numeros = random.sample(range(1, 61), quantidade)

        # Validação da quantidade de números
        if 6 <= len(numeros) <= 15:
            escritor.writerow([identificador] + numeros)