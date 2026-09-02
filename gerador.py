import csv
import random

with open("resultados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    for i in range(10):
        identificador = "AP-" + "".join(
            random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=6)
        )

        numeros = random.sample(range(1, 61), 6)

        escritor.writerow([identificador] + numeros)

        