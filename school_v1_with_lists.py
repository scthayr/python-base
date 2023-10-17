#!/usr/bin/env python3
"""Exibe relatório de alunos por atividade.

Imprimir a lista de alunos agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.0"

# Dados
sala1= ["Josh", "Aurora", "Sophie", "João", "Francisco"]
sala2 = ["Beto", "Joana", "Catarina", "Marta", "Katuxa"]

aula_ingles = ["Josh", "Aurora", "João", "Marta", "Joana"]
aula_musica = ["Josh", "João", "Marta"]
aula_danca = ["Beto", "Catarina", "Sophie", "Maria"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca),
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40)   
































































